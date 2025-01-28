#!/usr/bin/env python
'''
    test-generator
    ==============

    Auto-create the TOML test cases.

    This creates a TOML file with the contents similar to:
        [metadata]
        title = "Go - Decimal String - {version}"
        literal = false
        language = "go"
        description = "Go string decimal numbers parsed via `ParseFloat` and `ParseInt`."

        # Non-Digit Separator Flags

        [[floats]]  # TEST 0
        value = "0.1"
        title = "Simple"
        flags = ""
        outcome = "pass"
        expected = "0.1"

        [[ints]]   # TEST 0
        value = "12"
        title = "Simple"
        flags = ""
        outcome = "pass"
        expected = "12"

        [[floats]]  # TEST 1
        value = ".1"
        title = "Required integer digits."
        flags = "I/R"
        outcome = "fail"
        expected = "0.1"
'''

import typing
import argparse
import enum
import math
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

__version__ = '0.0.1'
__author__ = 'Alex Huszagh <ahuszagh@gmail.com>'

home = Path(__file__).absolute().parent.parent

_bool: typing.TypeAlias = bool
_int: typing.TypeAlias = int
_float: typing.TypeAlias = float
_str: typing.TypeAlias = str
_datetime: typing.TypeAlias = datetime
_array = list['_value']
_table = dict[str, '_value']
_value: typing.TypeAlias = _bool | _int | _float | _str | _datetime | _array | _table
_strs = _str | list[_str]


class Ansi:
    '''ANSI enum color codes.'''

    RESET: typing.ClassVar[str] = '\x1b[0m'

    @staticmethod
    def key(value: str) -> str:
        return f'\x1b[3;36m{value}\x1b[23;39m'

    @staticmethod
    def bool(value: str) -> str:
        return f'\x1b[38;5;27m{value}\x1b[39m'

    @staticmethod
    def number(value: str) -> str:
        return f'\x1b[38;5;82m{value}\x1b[39m'

    @staticmethod
    def datetime(value: str) -> str:
        return Ansi.number(value)

    @staticmethod
    def string(value: str) -> str:
        return f'\x1b[38;5;172m{value}\x1b[39m'

    @staticmethod
    def header(value: str) -> str:
        inner = f'\x1b[3;32m{value}\x1b[23;32m'
        start = '\x1b[1;35m'
        end = '\x1b[22;39m'
        return f'{start}[{end}{inner}{start}]{end}'

    @staticmethod
    def array(value: str) -> str:
        start = '\x1b[1;33m'
        end = '\x1b[22;39m'
        return f'{start}[{end}{Ansi.header(value)}{start}]{end}'

    @staticmethod
    def comment(value: str) -> str:
        return f'\x1b[2m{value}\x1b[22m'


@dataclass
class Logger:
    '''Custom logger that also logs to an output file.'''

    output: os.PathLike | None
    quiet: bool

    def log(self, message: str) -> None:
        '''Log our data to stdout, and optionally to file with no escape sequences.'''

        if not self.quiet:
            print(message)
        if self.output is None:
            return

        with open(self.output, mode='a+', encoding='utf-8') as file:
            no_ansi = re.sub(r'\x1b\[[0-9;]*m', '', message)
            print(no_ansi, file=file)


class Line(enum.Enum):
    SINGLE = enum.auto()
    MULTI = enum.auto()
    GUESS = enum.auto()


class TomlFormat:
    '''Static methods to help write TOML.'''

    @staticmethod
    def key(key: _str) -> _str:
        # NOTE: Keys can be empty but must be quotes
        use_bare = re.match(r'^[A-Za-z0-9_-]+$', key) is not None
        key = key if use_bare else TomlFormat.string(key, Line.SINGLE)
        return Ansi.key(key)

    @staticmethod
    def value(value: _value, multiline: Line = Line.GUESS, indent: int = 0) -> _str:
        # NOTE: Tables will always be single-line, arrays and strings can be multi
        if isinstance(value, _bool):
            return Ansi.bool(TomlFormat.bool(value))
        elif isinstance(value, _int):
            return Ansi.number(TomlFormat.int(value))
        elif isinstance(value, _float):
            return Ansi.number(TomlFormat.float(value))
        elif isinstance(value, _str):
            return Ansi.string(TomlFormat.string(value, multiline))
        elif isinstance(value, _datetime):
            return Ansi.datetime(TomlFormat.datetime(value))
        elif isinstance(value, list):
            return TomlFormat.array(value, multiline, indent)
        elif isinstance(value, dict):
            return TomlFormat.table(value, Line.SINGLE)
        cls_name = value.__class__.__name__
        raise TypeError(f'Got an invalid value type of "{cls_name}".')

    @staticmethod
    def pair(key: _str, value: _value, multiline: Line = Line.GUESS) -> _str:
        return f'{TomlFormat.key(key)} = {TomlFormat.value(value, multiline)}'

    @staticmethod
    def bool(value: _bool) -> _str:
        return 'true' if value else 'false'

    @staticmethod
    def int(value: _int) -> _str:
        return _str(value)

    @staticmethod
    def float(value: _float) -> _str:
        return _str(value)

    @staticmethod
    def _escape(value: _str, multiline: Line = Line.GUESS) -> _str:
        # NOTE: Don't skip tabs, and quotes which we handle above
        value = value.replace('\\', '\\\\')
        value = value.replace('\b', '\\b')
        value = value.replace('\f', '\\f')
        if multiline != Line.MULTI:
            value = value.replace('\n', '\\n')
            value = value.replace('\r', '\\r')
        return value

    @staticmethod
    def string(value: _str, multiline: Line = Line.GUESS) -> _str:
        lines = len(value.splitlines())
        if multiline == Line.MULTI:
            # NOTE: The first newline is trimmed in raw strings.
            value = TomlFormat._escape(value, Line.MULTI)
            if lines > 1:
                value = f'\n{value}'
            if '"""' not in value:
                return f'"""{value}"""'
            elif "'''" not in value:
                return f"'''{value}'''"
            escaped = value.replace('"""', '\"""')
            return f'"""{escaped}"""'

        if multiline == Line.GUESS and (lines > 1 or '"' in value):
            return TomlFormat.string(value, Line.MULTI)

        value = TomlFormat._escape(value, Line.SINGLE)
        if '"' not in value:
            return f'"{value}"'
        elif "'" not in value:
            return f"'{value}'"
        escaped = value.replace('"', '\"')
        return f'"{escaped}"'

    @staticmethod
    def datetime(value: _datetime) -> _str:
        return value.isoformat()

    @staticmethod
    def comment(value: _str) -> _str:
        lines = value.splitlines()
        return Ansi.comment('\n'.join([f'# {i}' for i in lines]))

    def array(value: _array, multiline: Line = Line.GUESS, indent: int = 0) -> _str:
        # NOTE: This does not support the `[[key]]` table format
        data = [TomlFormat.value(i, multiline, indent=indent + 2) for i in value]
        if multiline == Line.GUESS:
            length = sum(len(i) for i in data) + 2 * len(data)
            multiline = Line.SINGLE if length <= 80 else Line.MULTI

        if multiline == Line.MULTI:
            space = ' ' * (indent + 2)
            start = f'[\n{space}'
            end = '\n' + ' ' * indent + ']'
            return start + f',\n{space}'.join(data) + end

        return '[' + ', '.join(data) + ']'

    def table(value: _table, multiline: Line) -> _str:
        # NOTE: This does not support nested `[key.sub]` table format
        inner = Line.SINGLE if multiline == Line.SINGLE else Line.GUESS
        data = [TomlFormat.pair(k, v, inner) for k, v in value.items()]
        lines = sum(len(i.splitlines()) for i in data)
        if multiline == Line.SINGLE and lines > len(data):
            raise ValueError(f'A developer error occurred encoding the single-line table "{value}".')
        elif multiline == Line.GUESS:
            raise ValueError('Guessing the multi-line status of tables not allowed.')
        elif multiline == Line.SINGLE:
            joined = ', '.join(data)
            return f'{{ {joined} }}' if data else '{}'
        return '\n'.join(data)


def base_repr(n, base: int = 10):
    '''Convert a number to string with a given radix.'''

    if n < 0:
        return '-' + base_repr(-n, base)

    digits = []
    while n >= base:
        digits.append(str(n % base))
        n //= base
    digits.append(str(n % base))

    return ''.join(digits[::-1])


def swap_case(s: str) -> str:
    code = ord(s)
    if code > 127:
        raise ValueError('Exponent character must be in the ASCII plane.')
    if 0x61 <= code <= 0x7a:
        return chr(code - 0x20)
    elif 0x41 <= code <= 0x5a:
        return chr(code + 0x20)
    return s


@dataclass
class Case:
    '''A single test case metadata.'''

    index: int
    title: str
    flags: str
    outcome: str


cases: dict[int, Case] = {
    0: Case(
        index=0,
        title='Simple',
        flags='',
        outcome='pass',
    ),
    1: Case(
        index=1,
        title='Required integer digits.',
        flags='I/R',
        outcome='fail',
    ),
    2: Case(
        index=2,
        title='Required fraction digits.',
        flags='F/R',
        outcome='fail',
    ),
    3: Case(
        index=3,
        title='Required exponent digits.',
        flags='E/R',
        outcome='fail',
    ),
    4: Case(
        index=4,
        title='Required mantissa digits.',
        flags='M/R',
        outcome='fail',
    ),
    5: Case(
        index=5,
        title='No mantissa positive sign.',
        flags='+/M',
        outcome='fail',
    ),
    6: Case(
        index=6,
        title='Required positive sign.',
        flags='R/M',
        outcome='fail',
    ),
    7: Case(
        index=7,
        title='No exponent notation.',
        flags='e/e',
        outcome='fail',
    ),
    8: Case(
        index=8,
        title='No exponent positive sign.',
        flags='+/E',
        outcome='fail',
    ),
    9: Case(
        index=9,
        title='Required exponent sign.',
        flags='R/E',
        outcome='fail',
    ),
    10: Case(
        index=10,
        title='No exponent without fraction.',
        flags='e/F',
        outcome='fail',
    ),
    11: Case(
        index=11,
        title='Require integer digits with exponent.',
        flags='I/E',
        outcome='fail',
    ),
    12: Case(
        index=12,
        title='Require fraction digits with exponent.',
        flags='F/E',
        outcome='fail',
    ),
    13: Case(
        index=13,
        title='Require mantissa digits with exponent.',
        flags='M/E',
        outcome='fail',
    ),
    14: Case(
        index=14,
        title='No integer leading zeros.',
        flags='N/I',
        outcome='assert',
    ),
    15: Case(
        index=15,
        title='No float leading zeros.',
        flags='N/F',
        outcome='assert',
    ),
    16: Case(
        index=16,
        title='Required exponent notation.',
        flags='R/e',
        outcome='fail',
    ),
    17: Case(
        index=17,
        title='Case-sensitive exponent character.',
        flags='e/C',
        outcome='fail',
    ),
    18: Case(
        index=18,
        title='Integer internal digit separator.',
        flags='I/I',
        outcome='pass',
    ),
    19: Case(
        index=19,
        title='Fraction internal digit separator.',
        flags='F/I',
        outcome='pass',
    ),
    20: Case(
        index=20,
        title='Exponent internal digit separator.',
        flags='E/I',
        outcome='pass',
    ),
    21: Case(
        index=21,
        title='Integer leading digit separator.',
        flags='I/L',
        outcome='pass',
    ),
    22: Case(
        index=22,
        title='Fraction leading digit separator.',
        flags='F/L',
        outcome='pass',
    ),
    23: Case(
        index=23,
        title='Exponent leading digit separator.',
        flags='E/L',
        outcome='pass',
    ),
    24: Case(
        index=24,
        title='Integer trailing digit separator.',
        flags='I/T',
        outcome='pass',
    ),
    25: Case(
        index=25,
        title='Fraction trailing digit separator.',
        flags='F/T',
        outcome='pass',
    ),
    26: Case(
        index=26,
        title='Exponent trailing digit separator.',
        flags='E/T',
        outcome='pass',
    ),
    27: Case(
        index=27,
        title='Integer consecutive digit separator.',
        flags='I/C',
        outcome='pass',
    ),
    28: Case(
        index=28,
        title='Fraction consecutive digit separator.',
        flags='F/C',
        outcome='pass',
    ),
    29: Case(
        index=29,
        title='Exponent consecutive digit separator.',
        flags='E/C',
        outcome='pass',
    ),
    30: Case(
        index=30,
        title='Digit separator with empty integer.',
        flags='_/I',
        outcome='pass',
    ),
    31: Case(
        index=31,
        title='Consecutive digit separator with empty integer.',
        flags='\'/I',
        outcome='pass',
    ),
    32: Case(
        index=32,
        title='Digit separator with empty fraction.',
        flags='_/F',
        outcome='pass',
    ),
    33: Case(
        index=33,
        title='Consecutive digit separator with empty fraction.',
        flags='\'/F',
        outcome='pass',
    ),
    34: Case(
        index=34,
        title='Digit separator with empty mantissa.',
        flags='_/M',
        outcome='pass',
    ),
    35: Case(
        index=35,
        title='Consecutive digit separator with empty mantissa.',
        flags='\'/M',
        outcome='pass',
    ),
    36: Case(
        index=36,
        title='Digit separator with empty exponent.',
        flags='_/E',
        outcome='pass',
    ),
    37: Case(
        index=37,
        title='Consecutive digit separator with empty exponent.',
        flags='\'/E',
        outcome='pass',
    ),
    38: Case(
        index=38,
        title='No special (non-finite) values.',
        flags='S/S',
        outcome='fail',
    ),
    39: Case(
        index=39,
        title='Case-sensitive special (non-finite) values.',
        flags='S/c',
        outcome='fail',
    ),
    40: Case(
        index=40,
        title='Special (non-finite) digit separator.',
        flags='S/_',
        outcome='pass',
    ),
    41: Case(
        index=41,
        title='Consecutive special digit separator.',
        flags='S/C',
        outcome='pass',
    ),
    42: Case(
        index=42,
        title='Has a representation of NaN.',
        flags='h/N',
        outcome='pass',
    ),
    43: Case(
        index=43,
        title='Allows a positive sign before a representation of NaN.',
        flags='+/N',
        outcome='pass',
    ),
    44: Case(
        index=44,
        title='Allows a negative sign before a representation of NaN.',
        flags='-/N',
        outcome='pass',
    ),
    45: Case(
        index=45,
        title='Has a case-sensitive representation of NaN.',
        flags='c/N',
        outcome='fail',
    ),
    46: Case(
        index=46,
        title='Has a representation of short infinity.',
        flags='h/S',
        outcome='pass',
    ),
    47: Case(
        index=47,
        title='Allows a positive sign before a representation of short infinity.',
        flags='+/S',
        outcome='pass',
    ),
    48: Case(
        index=48,
        title='Allows a negative sign before a representation of short infinity.',
        flags='-/S',
        outcome='pass',
    ),
    49: Case(
        index=49,
        title='Has a case-sensitive representation of short infinity.',
        flags='c/S',
        outcome='fail',
    ),
    50: Case(
        index=50,
        title='Has a representation of long infinity.',
        flags='h/L',
        outcome='pass',
    ),
    51: Case(
        index=51,
        title='Allows a positive sign before a representation of long infinity.',
        flags='+/L',
        outcome='pass',
    ),
    52: Case(
        index=52,
        title='Allows a negative sign before a representation of long infinity.',
        flags='-/L',
        outcome='pass',
    ),
    53: Case(
        index=53,
        title='Has a case-sensitive representation of long infinity.',
        flags='c/L',
        outcome='fail',
    ),
    54: Case(
        index=54,
        title='Supports base prefixes.',
        flags='s/P',
        outcome='pass',
    ),
    55: Case(
        index=55,
        title='Does not support base prefixes.',
        flags='n/P',
        outcome='fail',
    ),
    56: Case(
        index=56,
        title='Case-sensitive base prefix.',
        flags='e/P',
        outcome='fail',
    ),
    57: Case(
        index=57,
        title='Require base prefixes.',
        flags='r/P',
        outcome='fail',
    ),
    58: Case(
        index=58,
        title='Supports base suffixes.',
        flags='s/S',
        outcome='pass',
    ),
    59: Case(
        index=59,
        title='Does not support base suffixes.',
        flags='n/S',
        outcome='fail',
    ),
    60: Case(
        index=60,
        title='Case-sensitive base suffix.',
        flags='e/S',
        outcome='fail',
    ),
    61: Case(
        index=61,
        title='Require base suffixes.',
        flags='r/S',
        outcome='fail',
    ),
    # TODO: Many more here
}


class Sign(enum.Enum):
    NONE = enum.auto()
    OPTIONAL = enum.auto()
    NO_POSITIVE = enum.auto()
    REQUIRED = enum.auto()

    def sign(self, is_negative: bool) -> str:
        match self:
            case Sign.NONE:
                if is_negative:
                    raise ValueError('Cannot have negative value with no signs.')
                return ''
            case Sign.OPTIONAL:
                return '-' if is_negative else ''
            case Sign.NO_POSITIVE:
                return '-' if is_negative else ''
            case Sign.REQUIRED:
                return '-' if is_negative else '+'
            case _:
                raise NotImplementedError('Unreachable')


@dataclass
class Generator:
    '''A test-case generator'''

    # the logger that writes the tests to file
    logger: Logger

    # the metadata for the generator
    title: str
    literal: bool
    language: str
    description: str

    mantissa_radix: int = 10
    exponent_base: int = -1
    exponent_radix: int = -1
    decimal_point: str = '.'
    exponent_char: str = 'e'
    digit_separator: str | None = '_'
    base_prefix: str | None = None
    base_suffix: str | None = None
    mantissa_sign: Sign = Sign.OPTIONAL
    exponent_sign: Sign = Sign.OPTIONAL
    nan_string: str = 'NaN'
    nan_expr: str | None = None
    inf_string: str = 'inf'
    inf_expr: str | None = None
    infinity_string: str = 'Infinity'
    infinity_expr: str | None = None
    # this is for the literal values to avoid comparing to exp notation
    no_exponent: bool = False
    no_floats: bool = False
    no_ints: bool = False
    no_uints: bool = False

    def __post_init__(self) -> None:
        if self.exponent_base < 0:
            self.exponent_base = self.mantissa_radix
        if self.exponent_radix < 0:
            self.exponent_radix = self.mantissa_radix
        if self.digit_separator is not None:
            assert ord(self.digit_separator) < 128
        if self.base_prefix is not None:
            assert ord(self.base_prefix) < 128
        if self.base_suffix is not None:
            assert ord(self.base_suffix) < 128

    def get_base_prefix(self) -> str:
        return f'0{self.base_prefix}' if self.base_prefix else ''

    def get_base_suffix(self) -> str:
        return self.base_suffix or ''

    @property
    def metadata(self) -> _table:
        '''Create the metadata table.'''

        metadata = {
            'title': self.title,
            'literal': self.literal,
            'language': self.language,
            'description': self.description,
        }

        if self.mantissa_radix == self.exponent_base and self.mantissa_radix == self.exponent_radix:
            metadata['radix'] = self.mantissa_radix
        else:
            metadata['mantissa-radix'] = self.mantissa_radix
            metadata['exponent-base'] = self.exponent_base
            metadata['exponent-radix'] = self.exponent_radix

        return metadata

    def case(self, actual: _strs, expected: _strs, index: int) -> _table:
        case = cases[index]
        return {
            'value': actual,
            'title': case.title,
            'flags': case.flags,
            'outcome': case.outcome,
            'expected': expected,
        }

    def print_case(self, header: str, actual: _strs, expected: _strs, index: int) -> str:
        case = self.case(actual=actual, expected=expected, index=index)
        self.logger.log(f'{self.array_header(header, index)}')
        self.logger.log(TomlFormat.table(case, Line.MULTI) + '\n')

    @staticmethod
    def array_header(header: str, index: int) -> str:
        comment = TomlFormat.comment(f'TEST {index}')
        return f'{Ansi.array(header)}  {comment}'

    def to_int_expected(self, value: int, sign: Sign | None = None) -> str:
        '''Returns the decimal literal value for the expected value.'''
        sign = self.mantissa_sign if sign is None else sign
        digits = str(abs(value))
        return sign.sign(value < 0) + digits

    def to_actual(
        self,
        value: str,
        sign: str | None = None,
        prefix: str | None = None,
        suffix: str | None = None,
        is_negative: bool = False,
    ) -> str:
        sign = self.mantissa_sign.sign(is_negative) if sign is None else sign
        prefix = self.get_base_prefix() if prefix is None else prefix
        suffix = self.get_base_suffix() if suffix is None else suffix
        return f'{sign}{prefix}{value}{suffix}'

    def to_int_actual(
        self,
        value: int | str,
        sign: str | None = None,
        prefix: str | None = None,
        suffix: str | None = None,
        is_negative: bool = False,
    ) -> str:
        '''Returns the base-prefix, radix value for the actual value.'''
        if isinstance(value, int):
            assert value >= 0
            value = base_repr(value, base=self.mantissa_radix)
        return self.to_actual(
            value=value,
            sign=sign,
            prefix=prefix,
            suffix=suffix,
            is_negative=is_negative,
        )

    def get_fraction_digits(self, value: int) -> int:
        '''Get the estimated number of digits to correctly represent the fraction.'''

        assert value >= 0
        if value == 0:
            return 1

        # NOTE: THIS IS NOT A GENERAL-PURPOSE SOLUTION, HOWEVER,
        # WE ASSUME SPECIAL CASES: THIS IS, THERE IS AN EXACT
        # REPRESENTATION.
        digits = int(math.floor(abs(math.log(value, 10))))
        scaled = value * (10 ** digits)
        if scaled < 1:
            digits += 1
        elif scaled > 10:
            digits -= 1

        # NOTE: Normally 17 digits is normally the amount required to
        # get an exact representation, unique in every case, and we
        # just hack it up here but since we're in a controlled environment
        # we don't need to worry about real corner cases.
        start_digits = digits
        scaled = value * (10 ** digits)
        while digits - start_digits < 17 and round(scaled) != scaled:
            digits += 1
            scaled = value * (10 ** digits)
        return digits

    def to_decimal(
        self,
        integer: int,
        fraction: int,
        exponent: int | None = None,
        digits: int | None = None,
        mantissa_sign: str | None = None,
        exponent_sign: str | None = None,
        is_negative: bool = False,
        no_exponent: bool | None = None,
    ) -> str:
        # NOTE: The integer is the raw integer value, same with the exponent,
        # while the fraction is relative to the mantissa radix, that is,
        # `fraction / radix^digits`
        # we want to be able to get our denominator
        if digits is None:
            digits = self.get_fraction_digits(fraction)
        denominator = self.mantissa_radix ** digits

        # need to normalize the exponent based on literals
        exponent = exponent or None
        if no_exponent is None:
            no_exponent = self.no_exponent
        if no_exponent and exponent is not None:
            factor = self.exponent_base ** exponent
            integer *= factor
            fraction *= factor
            integer += int(fraction // denominator)
            fraction %= denominator
            exponent = None

        # convert the decimal components over
        mantissa_sign = mantissa_sign or self.mantissa_sign.sign(is_negative)
        as_decimal = str(fraction / denominator)[2:]
        value = f'{mantissa_sign}{integer}{self.decimal_point}{as_decimal}'
        if exponent is not None:
            exponent_sign = exponent_sign or self.exponent_sign.sign(is_negative)
            value += f'{self.exponent_char}{exponent_sign}{exponent}'

        return value

    def print_simple(self) -> None:
        '''Write our simple test cases.'''

        factor = 1 + (self.mantissa_radix - 1) / self.mantissa_radix
        integer = int(self.mantissa_radix * factor)
        fraction = int(self.mantissa_radix // 2)

        # write our simple cases
        self.logger.log(TomlFormat.comment('Simple Cases') + '\n')
        integral = base_repr(integer, base=self.mantissa_radix)
        fractional = base_repr(fraction, base=self.mantissa_radix)
        self.print_case(
            header='floats',
            actual=self.to_actual(f'{integral}{self.decimal_point}{fractional}'),
            expected=self.to_decimal(integer, fraction, digits=1),
            index=0,
        )
        self.print_case(
            header='ints',
            actual=self.to_int_actual(integer),
            expected=self.to_int_expected(integer),
            index=0,
        )
        if not self.no_uints:
            self.print_case(
                header='uints',
                actual=self.to_int_actual(integer),
                expected=self.to_int_expected(integer),
                index=0,
            )

    def print_required_digits(self) -> None:
        '''Write if there are required digit test cases.'''

        if not self.no_ints:
            self.print_case(
                header='ints',
                actual=self.to_actual(''),
                expected=self.to_int_expected(1),
                index=1,
            )
        if not self.no_floats:
            self.print_case(
                header='floats',
                actual=self.to_actual(f'{self.decimal_point}1'),
                expected=self.to_decimal(0, 1, digits=1),
                index=1,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{self.decimal_point}'),
                expected=self.to_decimal(1, 0, digits=1),
                index=2,
            )
            self.print_case(
                header='floats',
                actual=[
                    self.to_actual(f'1{self.decimal_point}0{self.exponent_char}'),
                    self.to_actual(f'1{self.exponent_char}'),
                    self.to_actual(f'1{self.decimal_point}{self.exponent_char}'),
                ],
                expected=[
                    self.to_decimal(1, 0, digits=1),
                    self.to_decimal(1, 0, digits=1),
                    self.to_decimal(1, 0, digits=1),
                ],
                index=3,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual('.'),
                expected=self.to_decimal(0, 0, digits=1),
                index=4,
            )

    def print_mantissa_sign(self) -> None:
        '''Write if there are required or forbidden mantissa signs.'''

        if not self.no_ints:
            self.print_case(
                header='ints',
                actual=self.to_actual('1', sign='+'),
                expected=self.to_int_expected(1),
                index=5,
            )
            self.print_case(
                header='ints',
                actual=self.to_actual('1', sign=''),
                expected=self.to_int_expected(1),
                index=6,
            )
        if not self.no_floats:
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{self.decimal_point}0', sign='+'),
                expected=self.to_decimal(1, 0, digits=1),
                index=5,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{self.decimal_point}0', sign=''),
                expected=self.to_decimal(1, 0, digits=1),
                index=6,
            )

    def print_exponent_components(self) -> None:
        '''Write the logic of exponent components.'''

        if self.no_floats:
            return

        radix2 = self.mantissa_radix * self.mantissa_radix
        radix3 = self.mantissa_radix * radix2
        exp_sign = self.exponent_sign.sign(False)
        exp = base_repr(3, self.exponent_radix)
        self.print_case(
            header='floats',
            actual=self.to_actual(f'1{self.decimal_point}0{self.exponent_char}{exp_sign}{exp}'),
            expected=self.to_decimal(radix3, 0, digits=1),
            index=7,
        )
        self.print_case(
            header='floats',
            actual=self.to_actual(f'1{self.decimal_point}0{self.exponent_char}+{exp}'),
            expected=self.to_decimal(radix3, 0, digits=1),
            index=8,
        )
        self.print_case(
            header='floats',
            actual=self.to_actual(f'1{self.decimal_point}0{self.exponent_char}{exp}'),
            expected=self.to_decimal(radix3, 0, digits=1),
            index=9,
        )
        self.print_case(
            header='floats',
            actual=self.to_actual(f'1{self.exponent_char}{exp_sign}{exp}'),
            expected=self.to_decimal(radix3, 0, digits=1),
            index=10,
        )
        self.print_case(
            header='floats',
            actual=self.to_actual(f'1{self.decimal_point}{self.exponent_char}{exp_sign}{exp}'),
            expected=self.to_decimal(radix3, 0, digits=1),
            index=11,
        )
        self.print_case(
            header='floats',
            actual=self.to_actual(f'{self.decimal_point}1{self.exponent_char}{exp_sign}{exp}'),
            expected=self.to_decimal(radix2, 0, digits=1),
            index=12,
        )
        self.print_case(
            header='floats',
            actual=self.to_actual(f'{self.decimal_point}{self.exponent_char}{exp_sign}{exp}'),
            expected=self.to_decimal(0, 0, digits=1),
            index=13,
        )
        mantissa = f'{base_repr(3, self.mantissa_radix)}{self.decimal_point}1'
        self.print_case(
            header='floats',
            actual=self.to_actual(mantissa),
            expected=self.to_decimal(3, 1, digits=1),
            index=16,
        )
        self.print_case(
            header='floats',
            actual=self.to_actual(f'{mantissa}{swap_case(self.exponent_char)}{exp_sign}{exp}'),
            expected=self.to_decimal(3, 1, exponent=3, digits=1),
            index=17,
        )

    def print_leading_zeros(self) -> None:
        '''Write the logic of required leading zeros.'''

        # NOTE: We have the assertion errors to avoid octals
        radix = self.mantissa_radix
        if not self.no_ints:
            self.print_case(
                header='ints',
                actual=self.to_actual('0011'),
                expected=self.to_int_expected(radix + 1),
                index=14,
            )
        if not self.no_uints:
            self.print_case(
                header='uints',
                actual=self.to_actual('0011'),
                expected=self.to_int_expected(radix + 1),
                index=14,
            )
        if not self.no_floats:
            self.print_case(
                header='floats',
                actual=self.to_actual('0011.1'),
                expected=self.to_decimal(radix + 1, 1, digits=1),
                index=15,
            )

    def print_digit_separators(self) -> None:
        '''Print the digit separators for our numbers.'''

        radix = self.mantissa_radix
        sep = self.digit_separator
        if sep is None:
            return
        if not self.no_ints:
            pos = self.to_int_expected(radix + 1)
            neg = self.to_int_expected(-radix - 1, sign=Sign.OPTIONAL)
            has_prefix = self.base_prefix is not None
            use_neg = not has_prefix and self.mantissa_sign != Sign.NONE
            self.print_case(
                header='ints',
                actual=self.to_actual(f'1{sep}1'),
                expected=pos,
                index=18,
            )
            self.print_case(
                header='ints',
                actual=(
                    self.to_actual(f'{sep}11', sign='-') if use_neg
                    else self.to_actual(f'{sep}11')
                ),
                expected=neg if use_neg else pos,
                index=21,
            )
            self.print_case(
                header='ints',
                actual=self.to_actual(f'11{sep}'),
                expected=pos,
                index=24,
            )
            # NOTE: All of the consecutive ones need to be separate so they can
            # only be compared to ones where the value is valid.
            self.print_case(
                header='ints',
                actual=self.to_actual(f'1{sep}{sep}1'),
                expected=pos,
                index=27,
            )
            self.print_case(
                header='ints',
                actual=(
                    self.to_actual(f'{sep}{sep}11', sign='-') if use_neg
                    else self.to_actual(f'{sep}{sep}11')
                ),
                expected=neg if use_neg else pos,
                index=27,
            )
            self.print_case(
                header='ints',
                actual=self.to_actual(f'11{sep}{sep}'),
                expected=pos,
                index=27,
            )

        if not self.no_floats:
            dot = self.decimal_point
            exp_char = self.exponent_char
            exp_sign = self.exponent_sign.sign(False)
            pos = self.to_decimal(
                integer=radix + 1,
                fraction=radix + 1,
                digits=2,
            )
            neg = self.to_decimal(
                integer=radix + 1,
                fraction=radix + 1,
                digits=2,
                mantissa_sign='-',
            )
            pos_exp = self.to_decimal(
                integer=radix + 1,
                fraction=radix + 1,
                exponent=radix + 1,
                digits=2,
            )
            has_prefix = self.base_prefix is not None
            use_neg = not has_prefix and self.mantissa_sign != Sign.NONE
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{sep}1{dot}11'),
                expected=pos,
                index=18,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}1{sep}1'),
                expected=pos,
                index=19,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{exp_char}{exp_sign}1{sep}1'),
                expected=pos_exp,
                index=20,
            )
            self.print_case(
                header='floats',
                actual=(
                    self.to_actual(f'{sep}11{dot}11', sign='-') if use_neg
                    else self.to_actual(f'{sep}11{dot}11')
                ),
                expected=neg if use_neg else pos,
                index=21,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}{sep}11'),
                expected=pos,
                index=22,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{exp_char}{exp_sign}{sep}11'),
                expected=pos_exp,
                index=23,
            )
            self.print_case(
                header='ints',
                actual=self.to_actual(f'11{sep}{dot}11'),
                expected=pos,
                index=24,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{sep}'),
                expected=pos,
                index=25,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{sep}{exp_char}{exp_sign}11'),
                expected=pos_exp,
                index=25,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{exp_char}{exp_sign}11{sep}'),
                expected=pos_exp,
                index=26,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{sep}{sep}1{dot}11'),
                expected=pos,
                index=27,
            )
            self.print_case(
                header='floats',
                actual=(
                    self.to_actual(f'{sep}{sep}11{dot}11', sign='-') if use_neg
                    else self.to_actual(f'{sep}{sep}11{dot}11')
                ),
                expected=neg if use_neg else pos,
                index=27,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{sep}{sep}{dot}11'),
                expected=pos,
                index=27,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}1{sep}{sep}1'),
                expected=pos,
                index=28,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}{sep}{sep}11'),
                expected=pos,
                index=28,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{sep}{sep}'),
                expected=pos,
                index=28,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{sep}{sep}{exp_char}{exp_sign}11'),
                expected=pos_exp,
                index=28,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{exp_char}{exp_sign}1{sep}{sep}1'),
                expected=pos_exp,
                index=29,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{exp_char}{exp_sign}{sep}{sep}11'),
                expected=pos_exp,
                index=29,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11{exp_char}{exp_sign}11{sep}{sep}'),
                expected=pos_exp,
                index=29,
            )

    def print_empty_digit_separators(self) -> None:
        '''Print the empty digit separators for our numbers.'''

        sep = self.digit_separator
        if sep is None:
            return
        if not self.no_ints:
            dot = self.decimal_point
            self.print_case(
                header='ints',
                actual=self.to_actual(f'{sep}'),
                expected=self.to_int_expected(0),
                index=30,
            )
            self.print_case(
                header='ints',
                actual=self.to_actual(f'{sep}{sep}'),
                expected=self.to_int_expected(0),
                index=31,
            )
        if not self.no_floats:
            self.print_case(
                header='floats',
                actual=self.to_actual(f'{sep}'),
                expected=self.to_decimal(0, 0, digits=1),
                index=30,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'{sep}{dot}1'),
                expected=self.to_decimal(0, 1, digits=1),
                index=30,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'{sep}{sep}'),
                expected=self.to_decimal(0, 0, digits=1),
                index=31,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'{sep}{sep}{dot}{1}'),
                expected=self.to_decimal(0, 1, digits=1),
                index=31,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{dot}{sep}'),
                expected=self.to_decimal(1, 0, digits=1),
                index=32,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{dot}{sep}{sep}'),
                expected=self.to_decimal(1, 0, digits=1),
                index=33,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'{sep}{dot}{sep}'),
                expected=self.to_decimal(0, 0, digits=1),
                index=34,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'{sep}{sep}{dot}{sep}{sep}'),
                expected=self.to_decimal(0, 0, digits=1),
                index=35,
            )
            exp_char = self.exponent_char
            exp_sign = self.exponent_sign.sign(False)
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{dot}1{exp_char}{exp_sign}{sep}'),
                expected=self.to_decimal(1, 1, digits=1),
                index=36,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'1{dot}1{exp_char}{exp_sign}{sep}{sep}'),
                expected=self.to_decimal(1, 1, digits=1),
                index=37,
            )

    def print_specials(self) -> None:
        '''Print the test cases for various special character support.'''

        def case_permutations(s: str, n: int) -> list[str]:
            return [s[:i] + swap_case(s[i]) + s[i + 1:] for i in range(n)]

        def sep_permutations(s: str, n: int, c: int = 1) -> list[str]:
            sep = self.digit_separator
            return [s[:i] + sep * c + s[i:] for i in range(1, n + 1)]

        # NOTE: all specials do not support base prefixes/suffixes, etc.
        if self.no_floats:
            return

        # generic special
        nan_expr = self.nan_expr or self.nan_string
        inf_expr = self.inf_expr or self.inf_string
        infinity_expr = self.infinity_expr or self.infinity_string
        self.print_case(
            header='floats',
            actual=self.nan_string,
            expected=nan_expr,
            index=38,
        )
        self.print_case(
            header='floats',
            actual=case_permutations(self.nan_string, 2),
            expected=[nan_expr] * 2,
            index=39,
        )
        self.print_case(
            header='floats',
            actual=sep_permutations(self.nan_string, 3),
            expected=[nan_expr] * 3,
            index=40,
        )
        self.print_case(
            header='floats',
            actual=sep_permutations(self.nan_string, 3, 2),
            expected=[nan_expr] * 3,
            index=41,
        )

        # NaN
        self.print_case(
            header='floats',
            actual=self.nan_string,
            expected=nan_expr,
            index=42,
        )
        self.print_case(
            header='floats',
            actual='+' + self.nan_string,
            expected=nan_expr,
            index=43,
        )
        self.print_case(
            header='floats',
            actual='-' + self.nan_string,
            expected=nan_expr,
            index=44,
        )
        self.print_case(
            header='floats',
            actual=case_permutations(self.nan_string, 3),
            expected=[nan_expr] * 3,
            index=45,
        )

        # short infinity
        self.print_case(
            header='floats',
            actual=self.inf_string,
            expected=inf_expr,
            index=46,
        )
        self.print_case(
            header='floats',
            actual='+' + self.inf_string,
            expected=inf_expr,
            index=47,
        )
        self.print_case(
            header='floats',
            actual='-' + self.inf_string,
            expected='-' + inf_expr,
            index=48,
        )
        self.print_case(
            header='floats',
            actual=case_permutations(self.inf_string, 3),
            expected=[inf_expr] * 3,
            index=49,
        )

        # short infinity
        self.print_case(
            header='floats',
            actual=self.infinity_string,
            expected=infinity_expr,
            index=50,
        )
        self.print_case(
            header='floats',
            actual='+' + self.infinity_string,
            expected=infinity_expr,
            index=41,
        )
        self.print_case(
            header='floats',
            actual='-' + self.infinity_string,
            expected='-' + infinity_expr,
            index=52,
        )
        self.print_case(
            header='floats',
            actual=case_permutations(self.infinity_string, 3),
            expected=[infinity_expr] * 3,
            index=53,
        )

    def print_bases(self) -> None:
        '''Print the test cases for base prefix/suffix support.'''

        base_prefix = self.get_base_prefix() or '0d'
        base_suffix = self.get_base_suffix() or 'd'
        swap_prefix = '0' + swap_case(base_prefix[1])
        swap_suffix = swap_case(base_suffix)
        radix = self.mantissa_radix
        if not self.no_ints:
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', prefix=base_prefix),
                expected=self.to_int_expected(radix + 1),
                index=54,
            )
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', prefix=base_prefix),
                expected=self.to_int_expected(radix + 1),
                index=55,
            )
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', prefix=swap_prefix),
                expected=self.to_int_expected(radix + 1),
                index=56,
            )
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', prefix=''),
                expected=self.to_int_expected(radix + 1),
                index=57,
            )
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', suffix=base_suffix),
                expected=self.to_int_expected(radix + 1),
                index=58,
            )
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', suffix=base_suffix),
                expected=self.to_int_expected(radix + 1),
                index=59,
            )
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', suffix=swap_suffix),
                expected=self.to_int_expected(radix + 1),
                index=60,
            )
            self.print_case(
                header='ints',
                actual=self.to_int_actual('11', suffix=''),
                expected=self.to_int_expected(radix + 1),
                index=61,
            )

        if not self.no_floats:
            dot = self.decimal_point
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', prefix=base_prefix),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=54,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', prefix=base_prefix),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=55,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', prefix=swap_prefix),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=56,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', prefix=''),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=57,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', suffix=base_suffix),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=58,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', suffix=base_suffix),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=59,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', suffix=swap_suffix),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=60,
            )
            self.print_case(
                header='floats',
                actual=self.to_actual(f'11{dot}11', suffix=''),
                expected=self.to_decimal(radix + 1, radix + 1, digits=2),
                index=61,
            )

    def print_base_digit_separators(self) -> None:
        '''Print the test cases for base prefix/suffix digit separator support.'''
        raise NotImplementedError('TODO')

    def print(self) -> None:
        '''Print the generated test cases to file.'''

        self.logger.log(f'{Ansi.header("metadata")}')
        self.logger.log(TomlFormat.table(self.metadata, Line.MULTI) + '\n')
        self.print_simple()
        self.print_required_digits()
        self.print_mantissa_sign()
        self.print_exponent_components()
        self.print_leading_zeros()
        self.print_digit_separators()
        self.print_empty_digit_separators()
        self.print_specials()
        self.print_bases()
        self.print_base_digit_separators()


def create_from_config() -> None:
    '''Create all our test cases from a config file.'''
    raise NotImplementedError('TODO')


def main(argv: list[str] | None = None):
    '''Run our main entry point.'''

    global verbose

    parser = argparse.ArgumentParser(
        prog='test generator',
        description='number format test case generator for various programming languages.',
    )
    subparser = parser.add_subparsers(help='config or single-language parser', dest='subcommand')

    config_parser = subparser.add_parser('config', help='create test cases from config file')
    config_parser.add_argument(
        '-c',
        '--config',
        help='the path to the config file',
    )
    config_parser.add_argument(
        '-d',
        '--directory',
        help='the directory to save the generated tests to',
        default=home / 'data',
        type=Path,
    )

    lang_parser = subparser.add_parser('language', help='create test cases for a single language')
    lang_parser.add_argument(
        '-o',
        '--output',
        help='an optional path to write the data to file',
        type=Path,
    )
    lang_parser.add_argument(
        '--literal',
        action='store_true',
        help='if the tests are for number literals',
    )
    lang_parser.add_argument(
        '-t',
        '--title',
        required=True,
        help='a title to display for the results',
    )
    lang_parser.add_argument(
        '-l',
        '--language',
        required=True,
        help='the programming or data interchange format to test',
    )
    lang_parser.add_argument(
        '-d',
        '--description',
        required=True,
        help='the description to display under the title',
    )
    lang_parser.add_argument(
        '-r',
        '--radix',
        '--mantissa-radix',
        dest='mantissa_radix',
        default=10,
        type=int,
        help='the base for the significant digit numeric conversions',
    )
    lang_parser.add_argument(
        '--exponent-base',
        dest='exponent_base',
        default=-1,
        type=int,
        help='the base the exponent is raised to',
    )
    lang_parser.add_argument(
        '--exponent-radix',
        dest='exponent_radix',
        default=-1,
        type=int,
        help='the base for the exponent digit numeric conversions',
    )
    lang_parser.add_argument(
        '--digit-separator',
        default='_',
        help='the optional delimiter between digits, such as "_"',
    )
    lang_parser.add_argument(
        '--decimal-point',
        default='.',
        help='the character between the integer and fraction, such as "." or ","',
    )
    lang_parser.add_argument(
        '--exponent-char',
        default='e',
        help='the character between the mantissa and exponent, such as "e"',
    )
    lang_parser.add_argument(
        '--base-prefix',
        help='a character to signify the base at the start, such as "x" in `0x1`',
    )
    lang_parser.add_argument(
        '--base-suffix',
        help='a character to signify the base at the end, such as "h" in `1fd2h`',
    )
    lang_parser.add_argument(
        '--nan-string',
        default='NaN',
        help='the representation of NaN (as a literal or string), such as "NaN".',
    )
    lang_parser.add_argument(
        '--nan-expr',
        help='the expression that evaluates to NaN, such as `float("nan")`.',
    )
    lang_parser.add_argument(
        '--inf-string',
        default='inf',
        help='the representation of short infinity (as a literal or string), such as "Inf".',
    )
    lang_parser.add_argument(
        '--inf-expr',
        help='the short expression that evaluates to infinity, such as `float("inf")`.',
    )
    lang_parser.add_argument(
        '--infinity-string',
        default='Infinity',
        help='the representation of long infinity (as a literal or string), such as "Infinity".',
    )
    lang_parser.add_argument(
        '--infinity-expr',
        help='the long expression that evaluates to infinity, such as `float("infinity")`.',
    )
    lang_parser.add_argument(
        '--no-exponent',
        action='store_true',
        help='if the literal, validation cases do not support exponents.',
    )
    lang_parser.add_argument(
        '--no-floats',
        action='store_true',
        help='if the format does not support floating-point numbers.',
    )
    lang_parser.add_argument(
        '--no-ints',
        action='store_true',
        help='if the format does not support signed integers.',
    )
    lang_parser.add_argument(
        '--no-uints',
        action='store_true',
        help='if the format does not support unsigned integers.',
    )

    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version=f'%(prog)s {__version__}',
    )
    parser.add_argument(
        '-q',
        '--quiet',
        action='store_true',
        help='do not print output to console',
    )

    args = parser.parse_args(argv)
    match args.subcommand:
        case 'config':
            raise NotImplementedError('TODO')
        case 'language':
            if args.output is not None:
                Path(args.output).unlink(missing_ok=True)
            logger = Logger(args.output, args.quiet)
            generator = Generator(
                logger=logger,
                title=args.title,
                literal=args.literal,
                language=args.language,
                base_prefix=args.base_prefix,
                base_suffix=args.base_suffix,
                description=args.description,
                mantissa_radix=args.mantissa_radix,
                exponent_base=args.exponent_base,
                exponent_radix=args.exponent_radix,
                decimal_point=args.decimal_point,
                exponent_char=args.exponent_char,
                nan_string=args.nan_string,
                nan_expr=args.nan_expr,
                inf_string=args.inf_string,
                inf_expr=args.inf_expr,
                infinity_string=args.infinity_string,
                infinity_expr=args.infinity_expr,
                no_exponent=args.no_exponent,
                no_floats=args.no_floats,
                no_ints=args.no_ints,
                no_uints=args.no_uints,
            )
            generator.print()


if __name__ == '__main__':
    main()
