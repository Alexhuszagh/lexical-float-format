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

    Or these can be specified in a config file.
'''

import argparse
import copy
import os
import re
import shutil
import subprocess
import tomllib
import uuid
from dataclasses import dataclass
from pathlib import Path

__version__ = '0.0.1'
__author__ = 'Alex Huszagh <ahuszagh@gmail.com>'

home = Path(__file__).absolute().parent.parent
temp = home / 'temp'
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
    literal: str
    string: str
    extension: str
    floating: str
    integer: str
    # Optional override for the command
    command: str | None = None

    def template(self, literal: bool) -> str:
        '''Get the template string for the test.'''
        return self.literal if literal else self.string

    def build(self, code: str, literal: bool) -> subprocess.CompletedProcess:
        '''Build the code snippet, optionally running it, and returning the result.'''

        # build and process our results
        match self.name:
            case 'rust':
                return self._rust_build(code, literal)
            case 'python':
                return self._python_interpret(code, literal)
            case _:
                raise ValueError(f'Got an unsupported language of "{self.name}".')

    def get_version(self) -> str:
        '''Get the current version of the used interpreter.'''

        match self.name:
            case 'rust':
                return self._rustc_version
            case 'python':
                return self._python_version
            case _:
                raise ValueError(f'Got an unsupported language of "{self.name}".')

    def create_path(self) -> Path:
        '''Create a new, unique path for testing.'''
        return temp / f'{uuid.uuid4()}{self.extension}'

    def write_code(self, code: str) -> Path:
        '''Write our test code to a file for testing.'''
        path = self.create_path()
        with path.open(mode='w', encoding='utf-8') as file:
            file.write(code)
        return path

    # RUST

    @staticmethod
    def _getoutput(cmd: list[str]) -> str:
        if verbose:
            print('Command: ' + ' '.join(cmd))
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
        if verbose:
            print('Output: ' + result.stdout)
        return result.stdout

    @staticmethod
    def _run(cmd: list[str]) -> subprocess.CompletedProcess:
        if verbose:
            print('Running: ' + ' '.join(cmd))
        result = subprocess.run(cmd, capture_output=True, encoding='utf-8')
        if verbose:
            print('Received: ' + result.stdout)
        return result

    @property
    def _rustc(self) -> list[str]:
        if self.command is not None:
            return self.command.strip().split()
        return os.environ.get('RUSTC', 'rustc').strip().split()

    @property
    def _rustc_version(self) -> str:
        output = self._getoutput([*self._rustc, '--version'])
        return re.match(r'^rustc (\d+\.\d+(?:\.\d+)?).*$', output).group(1)

    def _rust_build(self, code: str, literal: bool) -> subprocess.CompletedProcess:
        '''Run our Rust compilation build and test.'''

        path = self.write_code(code)
        output = path.parent / path.stem
        result = self._run([*self._rustc, str(path), '-o', str(output)])
        if not literal and result.returncode != 0:
            raise RuntimeError(f'Got an unexpected result running code "{code}" for language "{repr(self)}".')
        if not literal:
            result = self._run([str(output)])

        return result

    # PYTHON

    @property
    def _python(self) -> list[str]:
        if self.command is not None:
            return self.command.strip().split()
        return os.environ.get('PYTHON', 'python').strip().split()

    @property
    def _python_version(self) -> str:
        output = self._getoutput([*self._python, '--version'])
        return re.match(r'^Python (\d+\.\d+(?:\.\d+)?).*$', output).group(1)

    def _python_interpret(self, code: str, literal: bool) -> subprocess.CompletedProcess:
        '''Interpret our Python code for testing.'''
        _ = literal
        return self._run([*self._python, '-c', code])


@dataclass
class File:
    '''A collection of test cases from a given file.'''

    path: Path
    metadata: 'Metadata'
    floats: list['Case']
    integers: list['Case']

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
                "integers": [...],
            }
        '''

        with path.open(encoding='utf-8') as file:
            data = tomllib.loads(file.read())

        metadata = Metadata(**data['metadata'])
        floats = [Case(**i) for i in data.get('floats', [])]
        integers = [Case(**i) for i in data.get('integers', [])]

        return cls(path=path, metadata=metadata, floats=floats, integers=integers)

    def run(self, command: str | None = None) -> str:
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
        language = self.get_language(command)
        version = language.get_version()
        title = self.metadata.title.format(version)
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
        for case in self.integers:
            result.append(case.run(
                language=language,
                literal=self.metadata.literal,
                data_type=language.integer,
                base=self.metadata.base,
            ))

        return '\n'.join(result)

    def get_language(self, command: str | None = None) -> Language:
        '''Get the language associated with the format version.'''
        return self.metadata.get_language(command)


@dataclass
class Metadata:
    '''Specifies the metadata for the test.'''

    title: str
    literal: bool
    language: str
    description: str | None = None
    base: int = 10

    def get_language(self, command: str | None = None) -> Language:
        '''Get the language specification from the name.'''

        language = languages[self.language]
        if command is not None:
            language = copy.copy(language)
            language.command = command
        return language


@dataclass
class Case:
    '''A single test case within the results.'''

    value: str | list[str]
    title: str
    flags: str = ''
    expected: str = 'pass'

    def succeeded(self, process: subprocess.CompletedProcess) -> bool:
        '''Determine if the process completed successfully.'''
        if self.expected == 'pass':
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
        data_type: str,
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
        data_type: str,
        base: int = 10,
    ) -> bool:
        '''Test one or more values and return if the test passed.'''
        fn = self.test_one if isinstance(self.value, str) else self.test_many
        return fn(
            language=language,
            value=self.value,
            literal=literal,
            data_type=data_type,
            base=base,
        )

    def test_one(
        self,
        language: Language,
        value: str,
        literal: bool,
        data_type: str,
        base: int = 10,
    ) -> bool:
        '''Run a test case for a single value.'''

        template = language.template(literal)
        code = template.format(type=data_type, value=value, base=base)
        process = language.build(code, literal)
        return self.succeeded(process)

    def test_many(
        self,
        language: Language,
        value: list[str],
        literal: bool,
        data_type: str,
        base: int = 10,
    ) -> bool:
        '''Run a test case for multiple values.'''

        results = [
            self.test_one(
                language=language,
                value=i,
                literal=literal,
                data_type=data_type,
                base=base,
            )
            for i in value
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
    config = {'language': {}}
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
        for command in commands:
            logger.log('\n' + case.run(command=command))


languages = {
    'rust': Language(
        name='rust',
        literal='''
pub fn main() {{
    let _: {type} = {value};
}}
''',
        string='''
pub fn main() {{
    let _ = "{value}".parse::<{type}>().unwrap();
}}
''',
        extension='.rs',
        floating='f64',
        integer='i64',
    ),
    'python': Language(
        name='python',
        literal='{value}',
        string='''
def as_int(x):
    return int(x, {base})

{type}("{value}")
''',
        extension='.py',
        floating='float',
        integer='as_int',
    )
}


if __name__ == '__main__':
    main()
