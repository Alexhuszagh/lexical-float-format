#!/usr/bin/env python
'''
    format-validator
    ================

    Run our main code formatter and check the
    validity of each from various data files.

    The compilers can be overwritten using the
    following environment variables:
    - `rustc`: `RUSTC`
    - `python`: `PYTHON`
    - `cc`: `CC`
    - `c++`: `CPP`
    - `julia`: `JULIA`
    - `node`: `NODE`

    Or these can be specified in a config file.
'''

import argparse
import copy
import itertools as it
import os
import re
import shutil
import subprocess
import tomllib
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

__version__ = '0.0.1'
__author__ = 'Alex Huszagh <ahuszagh@gmail.com>'

home = Path(__file__).absolute().parent.parent
temp = home / 'temp'
lang = home / 'lang'
verbose = False


@dataclass
class Logger:
    '''Custom logger that also logs to an output file.'''

    output: str | None

    def log(self, message: str) -> None:
        '''Log our data to stdout, and optionally to file with no escape sequences.'''

        print(message)
        if self.output is None:
            return

        with open(self.output, mode='a+', encoding='utf-8') as file:
            no_ansi = re.sub(r'\x1b\[[0-9;]*m', '', message)
            print(no_ansi, file=file)


@dataclass
class Language:
    '''Specification for a programming language or data interchange format.'''

    name: str
    literal: str | None
    string: str
    extension: str
    floating: str | None
    int: str | None
    uint: str | None
    # Optional override for the language version
    langversion: str | None = None
    # Optional override for the command
    command: str | None = None

    def template(self, literal: bool) -> str:
        '''Get the template string for the test.'''
        template = self.literal if literal else self.string
        if template is None:
            raise ValueError(f'Cannot use literal values for interchange format "{self.name}".')
        return template

    def build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Build the code snippet, optionally running it, and returning the result.'''

        build = getattr(self, f'_{self.name}_build', None)
        if build is None:
            raise ValueError(f'Got an unsupported language of "{self.name}".')
        return build(code, literal)

    def get_version(self) -> str:
        '''Get the current version of the used interpreter.'''

        version = getattr(self, f'_{self.name}_version', None)
        if version is None:
            raise ValueError(f'Got an unsupported language of "{self.name}".')
        return version

    def create_path(self, directory: Path = temp) -> Path:
        '''Create a new, unique path for testing.'''
        return directory / f'testing{self.extension}'

    def write_code(self, code: str) -> Path:
        '''Write our test code to a file for testing.'''
        # TODO: Might need our csproj or similar for some languages... SIGH
        path = self.create_path()
        with path.open(mode='w', encoding='utf-8') as file:
            file.write(code)
        return path

    # HELPERS

    @staticmethod
    def _split(value: str) -> list[str]:
        return value.strip().split()

    def _get_or_fallbacks(
        self,
        default: list[str],
        envvars: list[str] | None = None,
        fallbacks: list[str] | None = None,
    ) -> list[str]:
        '''Get the command, using environment variables or overrides if not found.'''

        if self.command is not None:
            return self._split(self.command)

        if envvars is not None:
            for envvar in envvars:
                cmd = os.environ.get(envvar)
                if cmd is not None:
                    return self._split(cmd)

        if fallbacks is not None:
            for fallback in fallbacks:
                if shutil.which(fallback) is not None:
                    return [fallback]

        return default

    @staticmethod
    def _getoutput(cmd: list[str]) -> str:
        if verbose:
            print('Command: ' + ' '.join(cmd))
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
        if verbose:
            print('Output: ' + result.stdout)
        return result.stdout

    @staticmethod
    def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
        if verbose:
            print('Running: ' + ' '.join(cmd))
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
        if verbose:
            print('Received: ' + result.stdout)
        return result

    def _build_and_test(
        self,
        code: str,
        literal: bool,
        cmd: Callable[[Path, Path], list[str]],
    ) -> subprocess.CompletedProcess[str]:
        '''Compile and optionally run the compiled code.'''

        path = self.write_code(code)
        output = path.parent / path.stem
        result = self._run(cmd(path, output))

        # compile-time failure is a test itself for literals
        if result.returncode != 0:
            if not literal:
                msg = f'Got an unexpected result compiling code "{code}" for language "{repr(self)}".'
                raise RuntimeError(msg)
            return result

        # if we have a mismatched value for our literals, then we have an issue
        result = self._run([str(output)])
        if result.returncode != 0 and literal:
            msg = f'Got an unexpected result running code "{code}" for language "{repr(self)}".'
            raise RuntimeError(msg)

        return result

    def _validate(
        self,
        code: str,
        literal: bool,
        process: subprocess.CompletedProcess[str],
        literal_errors: tuple[str, ...],
        parse_errors: tuple[str, ...],
        assertion_errors: tuple[str, ...],
    ) -> None:
        '''Validate the completed results from our code.'''

        is_success = process.returncode == 0

        # validate error handling
        if literal and not is_success:
            errors = literal_errors
        elif not literal and not is_success:
            errors = parse_errors
        else:
            errors = ()
        if not is_success and any(i in process.stdout for i in assertion_errors):
            raise AssertionError(f'Values did not equal for code "{code}".')
        if errors and not any(i in process.stdout for i in errors):
            raise ValueError(f'Got an unexpected response with error "{process.stdout}".')

    # RUST

    @property
    def _rustc(self) -> list[str]:
        return self._get_or_fallbacks(default=['rustc'], envvars=['RUSTC'])

    @property
    def _rust_version(self) -> str:
        output = self._getoutput([*self._rustc, '--version'])
        return re.match(r'^rustc (\d+\.\d+(?:\.\d+)?)', output).group(1)

    def _rust_build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Run our Rust compilation build and test.'''

        def to_cmd(input: Path, output: Path) -> str:
            return [*self._rustc, str(input), '-o', str(output)]

        process = self._build_and_test(code, literal, to_cmd)
        self._validate(
            code=code,
            literal=literal,
            process=process,
            literal_errors=('error:',),
            parse_errors=('`Err`',),
            assertion_errors=('assertion `left == right` failed',),
        )
        return process

    # PYTHON

    @property
    def _python(self) -> list[str]:
        return self._get_or_fallbacks(
            default=['python'],
            envvars=['PYTHON'],
            fallbacks=['python', 'python3', 'python2'],
        )

    @property
    def _python_version(self) -> str:
        output = self._getoutput([*self._python, '--version'])
        return re.match(r'^Python (\d+\.\d+(?:\.\d+)?)', output).group(1)

    def _python_build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Interpret our Python code for testing.'''

        process = self._run([*self._python, '-c', code])
        self._validate(
            code=code,
            literal=literal,
            process=process,
            literal_errors=('SyntaxError:', 'NameError:'),
            parse_errors=('ValueError:',),
            assertion_errors=('AssertionError:',),
        )
        return process

    # JULIA

    @property
    def _julia(self) -> list[str]:
        return self._get_or_fallbacks(
            default=['julia'],
            envvars=['JULIA'],
            fallbacks=['julia'],
        )

    @property
    def _julia_version(self) -> str:
        output = self._getoutput([*self._julia, '--version'])
        return re.match(r'^.*?(\d+\.\d+(?:\.\d+)?)', output).group(1)

    def _julia_build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Interpret our Python code for testing.'''

        process = self._run([*self._julia, '-e', code])
        self._validate(
            code=code,
            literal=literal,
            process=process,
            literal_errors=('ERROR: ParseError:', 'ERROR: UndefVarError:', 'ERROR: syntax:'),
            parse_errors=('ERROR: ArgumentError:',),
            assertion_errors=('ERROR: AssertionError:',),
        )
        return process

    # C

    @property
    def _cc(self) -> list[str]:
        return self._get_or_fallbacks(
            default=['cc'],
            envvars=['CC'],
            fallbacks=['cc', 'gcc', 'clang', 'cl'],
        )

    @property
    def _c_version(self) -> str:
        cc = self._cc
        if cc[0] in ('cl', 'cl.exe'):
            raise ValueError('MSVC is currently unsupported.')
        output = self._getoutput([*cc, '--version'])
        return re.match(r'^.*?(\d+\.\d+(?:\.\d+)?)', output).group(1)

    def _c_build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Run our C compilation build and test.'''

        def to_cmd(input: Path, output: Path) -> str:
            cmd = [*self._cc, str(input), '-o', str(output)]
            if self.langversion:
                cmd.append(f'-std={self.langversion}')
            return cmd

        return self._build_and_test(code, literal, to_cmd)

    # C++

    @property
    def _cpp(self) -> list[str]:
        return self._get_or_fallbacks(
            default=['c++'],
            envvars=['CPP'],
            fallbacks=['c++', 'g++', 'clang++', 'cl'],
        )

    @property
    def _cpp_version(self) -> str:
        cpp = self._cpp
        if cpp[0] in ('cl', 'cl.exe'):
            raise ValueError('MSVC is currently unsupported.')
        output = self._getoutput([*cpp, '--version'])
        return re.match(r'^.*?(\d+\.\d+(?:\.\d+)?)', output).group(1)

    def _cpp_build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Run our C compilation build and test.'''

        def to_cmd(input: Path, output: Path) -> str:
            cmd = [*self._cpp, str(input), '-o', str(output)]
            if self.langversion:
                cmd.append(f'-std={self.langversion}')
            return cmd

        return self._build_and_test(code, literal, to_cmd)

    # NODE

    @property
    def _node(self) -> list[str]:
        return self._get_or_fallbacks(
            default=['node'],
            envvars=['NODE'],
            fallbacks=['nodejs', 'node'],
        )

    @property
    def _node_version(self) -> str:
        output = self._getoutput([*self._node, '--version'])
        return re.match(r'^v(\d+\.\d+(?:\.\d+)?)', output).group(1)

    def _node_build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Interpret our Node.JS code for testing.'''
        raise NotImplementedError('TODO')

    # JSON

    @property
    def _json_version(self) -> str:
        # JSON has no version but is stable
        return "1.0"

    def _json_build(self, code: str, literal: bool) -> subprocess.CompletedProcess[str]:
        '''Interpret our Python code for testing.'''
        process = self._run([*self._node, '-e', code])
        self._validate(
            code=code,
            literal=literal,
            process=process,
            literal_errors=(),
            parse_errors=('SyntaxError:',),
            assertion_errors=('[ERR_ASSERTION]:',),
        )
        return process


@dataclass
class File:
    '''A collection of test cases from a given file.'''

    path: Path
    metadata: 'Metadata'
    floats: list['Case']
    ints: list['Case']
    uints: list['Case']

    @classmethod
    def load(cls, path: Path):
        '''
        Load the test data from the TOML file.

        The data format is similar to:
            {
                "metadata": {
                    "title": "",
                    "literal": "",
                    "language": "",
                },
                "floats": [...],
                "ints": [...],
                "uints": [...],
            }
        '''

        with path.open(encoding='utf-8') as file:
            data = tomllib.loads(file.read())

        metadata = Metadata(**data.pop('metadata'))
        floats = [Case(**i) for i in data.pop('floats', [])]
        ints = [Case(**i) for i in data.pop('ints', [])]
        uints = [Case(**i) for i in data.pop('uints', [])]

        return cls(path=path, metadata=metadata, floats=floats, ints=ints, uints=uints, **data)

    def run(self, command: str | None = None, langversion: str | None = None) -> str:
        '''
        Run the success or failure test cases.

        This returns the data formatted as a markdown table.

        For example:

            ## Rust - Binary Literal - 1.81.0

            Rust literal binary numbers. Requires base prefixes. Does not suppport floats.

            | Flag | Pass | Value | Title |
            |:-:|:-:|:-:|:-:|
            |  | ❌ | 0b0.1 | Simple |
            | N/I | ❌ | 0b001 | No integer leading zeros. |
            | e/P | ✅ | 0B1 | Case-sensitive base prefix. |
        '''

        # create our header
        language = self.get_language(command, langversion)
        version = language.get_version()
        title = self.metadata.title.format(version=version, lang=langversion)
        result = [f'## \x1b[1;36m{title}\x1b[0m', '']
        if self.metadata.description is not None:
            result += [self.metadata.description, '']
        result += ['| Flag | Pass | Value | Title |', '|:-:|:-:|:-:|:-:|']

        # run all our test cases
        for case in self.floats:
            result.append(case.run(
                language=language,
                literal=self.metadata.literal,
                data_type=language.floating,
                base=self.metadata.base,
            ))
        for case in self.ints:
            result.append(case.run(
                language=language,
                literal=self.metadata.literal,
                data_type=language.int,
                base=self.metadata.base,
            ))
        for case in self.uints:
            result.append(case.run(
                language=language,
                literal=self.metadata.literal,
                data_type=language.uint,
                base=self.metadata.base,
            ))

        return '\n'.join(result)

    def get_language(self, command: str | None = None, langversion: str | None = None) -> Language:
        '''Get the language associated with the format version.'''
        return self.metadata.get_language(command, langversion)


@dataclass
class Metadata:
    '''Specifies the metadata for the test.'''

    title: str
    literal: bool
    language: str
    description: str | None = None
    base: int = 10

    def get_language(self, command: str | None = None, langversion: str | None = None) -> Language:
        '''Get the language specification from the name.'''

        language = copy.copy(languages[self.language])
        if command is not None:
            language.command = command
        if langversion is not None:
            language.langversion = langversion
        return language


@dataclass
class Case:
    '''A single test case within the results.'''

    value: str | list[str]
    title: str
    expected: str | list[str]
    outcome: str
    flags: str

    def __post_init__(self):
        if self.outcome not in ('pass', 'fail'):
            raise ValueError('Outcome must be either "pass" or "fail".')

    def succeeded(self, process: subprocess.CompletedProcess) -> bool:
        '''Determine if the process completed successfully.'''
        if self.outcome == 'pass':
            return process.returncode == 0
        return process.returncode != 0

    @staticmethod
    def checkmark(success: bool) -> str:
        '''Convert the success or failure to a checkmark.'''
        return '✅' if success else '❌'

    def run(
        self,
        language: Language,
        literal: bool,
        data_type: str | None,
        base: int = 10,
    ) -> str:
        '''Run a single test case for a given language.'''

        success = self.test(
            language=language,
            literal=literal,
            data_type=data_type,
            base=base,
        )
        check = self.checkmark(success)
        value = self.value if isinstance(self.value, str) else self.value[0]

        return f'| {self.flags} | {check} | {value} | {self.title} |'

    def test(
        self,
        language: Language,
        literal: bool,
        data_type: str | None,
        base: int = 10,
    ) -> bool:
        '''Test one or more values and return if the test passed.'''
        fn = self.test_one if isinstance(self.value, str) else self.test_many
        return fn(
            language=language,
            value=self.value,
            expected=self.expected,
            literal=literal,
            data_type=data_type,
            base=base,
        )

    def test_one(
        self,
        language: Language,
        value: str,
        expected: str,
        literal: bool,
        data_type: str | None,
        base: int = 10,
    ) -> bool:
        '''Run a test case for a single value.'''

        template = language.template(literal)
        code = template.format(
            type=data_type,
            value=value,
            base=base,
            expected=expected,
        )
        process = language.build(code, literal)
        return self.succeeded(process)

    def test_many(
        self,
        language: Language,
        value: list[str],
        expected: list[str],
        literal: bool,
        data_type: str | None,
        base: int = 10,
    ) -> bool:
        '''Run a test case for multiple values.'''

        results = [
            self.test_one(
                language=language,
                value=value[i],
                expected=expected[i],
                literal=literal,
                data_type=data_type,
                base=base,
            )
            for i in range(len(value))
        ]
        if not all(i == results[0] for i in results[1:]):
            raise ValueError(f'Got inconsistent results for "{repr(self)}".')

        return results[0]


def main(argv: list[str] | None = None):
    '''Run our main entry point.'''

    global verbose

    parser = argparse.ArgumentParser(
        prog='format validator',
        description='Number format validator for various programming languages.',
    )
    parser.add_argument('-f', '--file', nargs='*', help='a list of files to process')
    parser.add_argument('-d', '--directory', nargs='*', help='a directory of files to process')
    parser.add_argument('-o', '--output', help='an optional path to write the data to file')
    parser.add_argument('-c', '--config', help='an optional config file to load')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}')
    args = parser.parse_args(argv)

    # ensure we print everything to stdout if we're piping the process
    verbose = args.verbose

    # load our config
    config = {'language': {}, 'langversion': {}}
    if args.config is not None:
        with Path(args.config).open(encoding='utf-8') as file:
            config = tomllib.loads(file.read())

    # cleanup a previous run, if it exists
    shutil.rmtree(temp, ignore_errors=True)
    temp.mkdir(exist_ok=True)

    # load all our test files
    files: list[Path] = []
    if args.file is not None:
        files += [Path(file) for file in args.file]
    if args.directory is not None:
        for directory in args.directory:
            files += [file for file in Path(directory).rglob('*.toml')]

    # load all our test cases from these files
    cases: list['File'] = [File.load(i) for i in files]

    # run our test cases and print our results
    logger = Logger(args.output)
    logger.log('# \x1b[1;32mResults\x1b[0m')
    for case in cases:
        commands = config['language'].get(case.metadata.language, [None])
        langversions = config['langversion'].get(case.metadata.language, [None])
        for command, langversion in it.product(commands, langversions):
            logger.log('\n' + case.run(command=command, langversion=langversion))


def read_string(path: Path) -> str:
    '''Read a file to string.'''
    with path.open(encoding='utf-8') as file:
        return file.read()


languages = {
    'rust': Language(
        name='rust',
        literal=read_string(lang / 'literal.rs'),
        string=read_string(lang / 'string.rs'),
        extension='.rs',
        floating='f64',
        int='i64',
        uint='u64',
    ),
    'python': Language(
        name='python',
        literal=read_string(lang / 'literal.py'),
        string=read_string(lang / 'string.py'),
        extension='.py',
        floating='float',
        int='int',
        uint='int',
    ),
    'c': Language(
        name='c',
        literal=read_string(lang / 'literal.c'),
        string=read_string(lang / 'string.c'),
        extension='.c',
        floating='f64',
        int='i32',
        uint='u32',
    ),
    'cpp': Language(
        name='cpp',
        literal=read_string(lang / 'literal.cpp'),
        string=read_string(lang / 'string.cpp'),
        extension='.cpp',
        floating='f64',
        int='i32',
        uint='u32',
    ),
    'julia': Language(
        name='julia',
        literal=read_string(lang / 'literal.jl'),
        string=read_string(lang / 'string.jl'),
        extension='.jl',
        floating='Float64',
        int='Int32',
        uint='UInt32',
    ),
    'json': Language(
        name='json',
        literal=None,
        string=read_string(lang / 'json.js'),
        extension='.json',
        floating=None,
        int=None,
        uint=None,
    ),
}


if __name__ == '__main__':
    main()
