#!/usr/bin/env python
'''
    format-validator
    ================

    Run our main code formatter and check the
    validity of each from various data files.

    The compilers can be overwritten using the
    following environment variables:
    - `rustc`: `RUSTC`
'''

import argparse
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
subprocess_kwds = {
    'stdout': subprocess.DEVNULL,
    'stderr': subprocess.DEVNULL,
}


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

    def template(self, literal: bool) -> str:
        '''Get the template string for the test.'''
        return self.literal if literal else self.string

    def build(self, code: str, literal: bool) -> subprocess.CompletedProcess:
        '''Build the code snippet, optionally running it, and returning the result.'''

        # build and process our results
        match self.name:
            case 'rust':
                return self._rust_build(code, literal)
            case _:
                raise ValueError(f'Got an unsupported language of "{self.name}".')

    def get_version(self) -> str:
        '''Get the current version of the used interpreter.'''

        match self.name:
            case 'rust':
                return self._rustc_version
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

    @property
    def _rustc(self) -> str:
        return os.environ.get('RUSTC', 'rustc')

    @property
    def _rustc_version(self) -> str:
        output = subprocess.getoutput([self._rustc, '--version'])
        return re.match(r'^rustc (\d+\.\d+(?:\.\d+)?) .*$', output).group(1)

    def _rust_build(self, code: str, literal: bool) -> subprocess.CompletedProcess:
        '''Run our Rust compilation build and test.'''

        path = self.write_code(code)
        output = path.parent / path.stem
        result = subprocess.run([self._rustc, str(path), '-o', str(output)], **subprocess_kwds)
        if not literal and result.returncode != 0:
            raise RuntimeError(f'Got an unexpected result running code "{code}" for language "{repr(self)}".')
        if not literal:
            result = subprocess.run([str(output)], **subprocess_kwds)

        return result


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

    def run(self) -> str:
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
        language = self.get_language()
        version = language.get_version()
        title = self.metadata.title.format(version)
        result = [f'## \x1b[1;36m{title}\x1b[0m', '']
        if self.metadata.description is not None:
            result += [self.metadata.description, '']
        result += ['| Flag | Pass | Value | Title |', '|:-:|:-:|:-:|:-:|']

        # run all our test cases
        for case in self.floats:
            result.append(case.run(language, self.metadata.literal, language.floating))
        for case in self.integers:
            result.append(case.run(language, self.metadata.literal, language.integer))

        return '\n'.join(result)

    def get_language(self) -> Language:
        '''Get the language associated with the format version.'''
        return self.metadata.get_language()


@dataclass
class Metadata:
    '''Specifies the metadata for the test.'''

    title: str
    literal: bool
    language: str
    description: str | None = None

    def get_language(self) -> Language:
        '''Get the language specification from the name.'''
        return languages[self.language]


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

    def run(self, language: Language, literal: bool, data_type: str) -> str:
        '''Run a single test case for a given language.'''
        check = self.checkmark(self.test(language, literal, data_type))
        value = self.value if isinstance(self.value, str) else self.value[0]
        return f'| {self.flags} | {check} | {value} | {self.title} |'

    def test(self, language: Language, literal: bool, data_type: str) -> bool:
        '''Test one or more values and return if the test passed.'''
        if isinstance(self.value, str):
            return self.test_one(language, self.value, literal, data_type)
        return self.test_many(language, self.value, literal, data_type)

    def test_one(self, language: Language, value: str, literal: bool, data_type: str) -> bool:
        '''Run a test case for a single value.'''
        template = language.template(literal)
        code = template.format(type=data_type, value=value)
        process = language.build(code, literal)
        return self.succeeded(process)

    def test_many(self, language: Language, values: list[str], literal: bool, data_type: str) -> bool:
        '''Run a test case for multiple values.'''
        results = [self.test_one(language, i, literal, data_type) for i in values]
        if not all(i == results[0] for i in results[1:]):
            raise ValueError(f'Got inconsistent results for "{repr(self)}".')
        return results[0]


def main(argv: list[str] | None = None):
    '''Run our main entry point.'''

    parser = argparse.ArgumentParser(
        prog='format validator',
        description='Number format validator for various programming languages.',
    )
    parser.add_argument('-f', '--file', nargs='*', help='a list of files to process')
    parser.add_argument('-d', '--directory', nargs='*', help='a directory of files to process')
    parser.add_argument('-o', '--output', help='an optional path to write the data to file')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}')
    args = parser.parse_args(argv)

    # ensure we print everything to stdout if we're piping the process
    if args.verbose:
        subprocess_kwds['stdout'] = subprocess.STDOUT
        subprocess_kwds['stderr'] = subprocess.STDOUT

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
        logger.log('\n' + case.run())


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
    )
}


if __name__ == '__main__':
    main()
