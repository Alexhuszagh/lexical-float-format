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

import typing
import argparse
import os
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
class TestFile:
    format: 'TestFormat'
    floats: list['TestCase']
    integers: list['TestCase']

    @classmethod
    def load(cls, data: dict[str, typing.Any]):
        format = TestFormat(**data['format'])
        floats = [TestCase(**i) for i in data.get('floats', [])]
        integers = [TestCase(**i) for i in data.get('integers', [])]
        return cls(format=format, floats=floats, integers=integers)

    def run(self, output: str | None = None) -> str:
        result = [f'## \x1b[1;36m{self.format.title}\x1b[0m', '']
        if self.format.description is not None:
            result += [self.format.description, '']
        result += ['| Flag | Pass | Value | Title |', '|:-:|:-:|:-:|:-:|']
        language = self.format.language
        literal = self.format.literal
        for case in self.floats:
            result.append(case.test(language, literal, types[(language, 'float')]))
        for case in self.integers:
            result.append(case.test(language, literal, types[(language, 'integer')]))

        print('\n' + '\n'.join(result))
        if output is not None:
            result[0] = f'## {self.format.title}'
            with open(output, mode='a+', encoding='utf-8') as file:
                print('\n' + '\n'.join(result), file=file)


@dataclass
class TestFormat:
    title: str
    literal: bool
    language: str
    description: str | None = None


@dataclass
class TestCase:
    value: str | list[str]
    title: str
    flags: str = ''
    supported: str = 'pass'

    def test(self, language: str, literal: bool, type: str) -> str:
        success = self.run(language, literal, type)
        code = '✅' if success else '❌'
        value = self.value if isinstance(self.value, str) else self.value[0]
        return f'| {self.flags} | {code} | {value} | {self.title} |'

    def run(self, language: str, literal: bool, type: str) -> bool:
        if isinstance(self.value, str):
            return self.run_one(self.value, language, literal, type)
        results = [self.run_one(i, language, literal, type) for i in self.value]
        if not all(i == results[0] for i in results[1:]):
            raise ValueError(f'Got inconsistent results for "{repr(self)}".')
        return results[0]

    def run_one(self, value: str, language: str, literal: bool, type: str) -> bool:
        template = templates[(language, literal)]
        code = template.format(type=type, value=value)
        path = temp / f'{uuid.uuid4()}{extensions[language]}'
        with path.open(mode='w', encoding='utf-8') as file:
            file.write(code)
        try:
            match language:
                case 'rust':
                    return self.rust(path, literal)
                case _:
                    raise ValueError(f'Got an unknown language of "{language}".')
        finally:
            path.unlink(missing_ok=True)

    def rust(self, path: Path, literal: bool) -> bool:
        rustc = os.environ.get('RUSTC', 'rustc')
        output = path.parent / path.stem
        result = subprocess.run([rustc, str(path), '-o', str(output)], **subprocess_kwds)
        if not literal and result.returncode != 0:
            raise RuntimeError(f'Got an unexpected result running test "{repr(self)}".')
        if not literal:
            result = subprocess.run([str(output)], **subprocess_kwds)
        if self.supported == 'pass':
            return result.returncode == 0
        return result.returncode != 0


def main(argv: list[str] | None = None):
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

    if args.verbose:
        subprocess_kwds['stdout'] = subprocess.STDOUT
        subprocess_kwds['stderr'] = subprocess.STDOUT

    shutil.rmtree(temp, ignore_errors=True)
    temp.mkdir(exist_ok=True)

    files: list[Path] = []
    if args.file is not None:
        files += [Path(file) for file in args.file]
    if args.directory is not None:
        for directory in args.directory:
            files += [file for file in Path(directory).rglob('*.toml')]

    cases: list['TestFile'] = []
    for file in files:
        with file.open(encoding='utf-8') as f:
            cases.append(TestFile.load(tomllib.loads(f.read())))
    print('# \x1b[1;32mResults\x1b[0m')
    if args.output is not None:
        with open(args.output, mode='a+', encoding='utf-8') as file:
            print('# Results', file=file)
    for case in cases:
        case.run(args.output)


rust_literal = '''
pub fn main() {{
    let _: {type} = {value};
}}
'''

rust_string = '''
pub fn main() {{
    let _ = "{value}".parse::<{type}>().unwrap();
}}
'''

templates = {
    ('rust', True): rust_literal,
    ('rust', False): rust_string,
}
extensions = {
    'rust': '.rs',
}
types = {
    ('rust', 'float'): 'f64',
    ('rust', 'integer'): 'i64',
}


if __name__ == '__main__':
    main()
