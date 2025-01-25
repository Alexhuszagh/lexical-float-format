# Results

## Rust

### Binary Literal - 1.81.0

Rust literal binary numbers. Requires base prefixes. Does not suppport floats.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ❌ | 0b0.1 | Simple |
| N/I | ❌ | 0b001 | No integer leading zeros. |
| e/P | ✅ | 0B1 | Case-sensitive base prefix. |
| e/S | ❌ | 0b1B | Case-sensitive base suffix. |
| M/R | ✅ | 0b | Required mantissa digits. |
| I/R | ✅ | 0b | Required integer digits. |
| +/M | ✅ | +0b1 | No mantissa positive sign. |
| R/M | ❌ | 0b1 | Required positive sign. |
| I/I | ✅ | 0b1_1 | Integer internal digit separator. |
| I/L | ✅ | 0b_11 | Integer leading digit separator. |
| I/T | ✅ | 0b11_ | Integer trailing digit separator. |
| I/C | ✅ | 0b1__1 | Integer consecutive digit separator. |
| s/D | ❌ | _0b11 | Absolute start digit separator. |
| I/s | ❌ | _-0b11 | Integer sign digit separator. |
| I/c | ❌ | __-0b11 | Integer sign consecutive digit separator. |

### Decimal Literal - 1.81.0

Rust literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ✅ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ✅ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ✅ | .1E3 | Require integer digits with exponent. |
| F/E | ✅ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ✅ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ✅ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ✅ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ✅ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ✅ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ✅ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ✅ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 1.81.0

Parsing numbers via `FromStr`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Hex Literal - 1.81.0

Rust literal hexadecimal numbers. Requires base prefixes. Does not suppport floats.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ❌ | 0x0.1 | Simple |
| N/I | ❌ | 0x001 | No integer leading zeros. |
| e/P | ✅ | 0X1 | Case-sensitive base prefix. |
| e/S | ❌ | 0x1X | Case-sensitive base suffix. |
| M/R | ✅ | 0x | Required mantissa digits. |
| I/R | ✅ | 0x | Required integer digits. |
| +/M | ✅ | +0x1 | No mantissa positive sign. |
| R/M | ❌ | 0x1 | Required positive sign. |
| I/I | ✅ | 0x1_1 | Integer internal digit separator. |
| I/L | ✅ | 0x_11 | Integer leading digit separator. |
| I/T | ✅ | 0x11_ | Integer trailing digit separator. |
| I/C | ✅ | 0x1__1 | Integer consecutive digit separator. |
| s/D | ❌ | _0x11 | Absolute start digit separator. |
| I/s | ❌ | _-0x11 | Integer sign digit separator. |
| I/c | ❌ | __-0x11 | Integer sign consecutive digit separator. |

### Octal Literal - 1.81.0

Rust literal octal numbers. Requires base prefixes. Does not suppport floats.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ❌ | 0o0.1 | Simple |
| N/I | ❌ | 0o001 | No integer leading zeros. |
| e/P | ✅ | 0O1 | Case-sensitive base prefix. |
| e/S | ❌ | 0o1O | Case-sensitive base suffix. |
| M/R | ✅ | 0o | Required mantissa digits. |
| I/R | ✅ | 0o | Required integer digits. |
| +/M | ✅ | +0o1 | No mantissa positive sign. |
| R/M | ❌ | 0o1 | Required positive sign. |
| I/I | ✅ | 0o1_1 | Integer internal digit separator. |
| I/L | ✅ | 0o_11 | Integer leading digit separator. |
| I/T | ✅ | 0o11_ | Integer trailing digit separator. |
| I/C | ✅ | 0o1__1 | Integer consecutive digit separator. |
| s/D | ❌ | _0o11 | Absolute start digit separator. |
| I/s | ❌ | _-0o11 | Integer sign digit separator. |
| I/c | ❌ | __-0o11 | Integer sign consecutive digit separator. |

## Python

### Decimal Literal - 2.7.18

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 2.7.18

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.3.5

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.3.5

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.4.4

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.4.4

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.5.4

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.5.4

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.6.8

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.6.8

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.7.9

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.7.9

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.8.10

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.8.10

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.9.2

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.9.2

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.10.0

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.10.0

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.11.9

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.11.9

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.12.0

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.12.0

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal Literal - 3.13.1

Python literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ✅ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

### Decimal String - 3.13.1

Parsing numbers via `float` or `int`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.0 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | INF | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.0 | No float leading zeros. |
| R/e | ❌ | 1.0 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1 | Require base prefixes. |
| r/S | ❌ | 1d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 001 | No integer leading zeros. |
| e/P | ❌ | 0D1 | Case-sensitive base prefix. |
| e/S | ❌ | 1D | Case-sensitive base suffix. |

## C

### Decimal Literal - 13.3.0 - Default

C literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c89

C literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c90

C literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c99

C literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c11

C literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c17

C literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - Default

C string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c89

C string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c90

C string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c99

C string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c11

C string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c17

C string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

## C++

### Decimal Literal - 13.3.0 - Default

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c++98

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c++03

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c++11

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c++14

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c++17

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c++20

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal Literal - 13.3.0 - c++23

C++ literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ✅ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ✅ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - Default

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c++98

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c++03

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c++11

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c++14

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c++17

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c++20

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 13.3.0 - c++23

C++ string decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ❌ | 1'1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1'1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1'1 | Exponent internal digit separator. |
| I/L | ❌ | -'11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11.'11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e'11 | Exponent leading digit separator. |
| I/T | ❌ | 11'.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11'e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11' | Exponent trailing digit separator. |
| I/C | ❌ | 1''1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1''1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1''1 | Exponent consecutive digit separator. |
| S/D | ❌ | N'a'N | Special (non-finite) digit separator. |
| s/D | ❌ | '11.11e11 | Absolute start digit separator. |
| I/s | ❌ | '-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | ''-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e'-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e''-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0'd11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -'0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d'11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d''11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11'd | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d' | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d'' | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

## Julia

### Decimal Literal - 1.11.2

Julia literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.2 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ✅ | inf64 | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d12 | Require base prefixes. |
| r/S | ❌ | 12d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 1.11.2

Parsing numbers via `Float64`, `Int64`, or `UInt64`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.2 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NaN | No special (non-finite) values. |
| S/C | ❌ | inf | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d12 | Require base prefixes. |
| r/S | ❌ | 12d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
| I/I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ✅ | -0 | No unsigned integer negative sign. |

## Go

### Decimal Literal - 1.22.2

Go literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NAN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ❌ | -0 | No unsigned integer negative sign. |

### Decimal String - 1.22.2

Go string decimal numbers parsed via `ParseFloat` and `ParseInt`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ❌ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ❌ | NAN | No special (non-finite) values. |
| S/C | ❌ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ❌ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ❌ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
| -/U | ✅ | -0 | No unsigned integer negative sign. |

## Ruby

### Decimal Literal - 3.2.3

Ruby literal decimal numbers. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ✅ | .1 | Required integer digits. |
| F/R | ✅ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ✅ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ✅ | .1E3 | Require integer digits with exponent. |
| F/E | ✅ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ✅ | 0012X | No integer leading zeros. |
| e/P | ✅ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |

### Decimal String - 3.2.3

Go string decimal numbers parsed via `Float` and `Integer`. Does not support base prefixes.

| Flag | Pass | Value | Title |
|:-:|:-:|:-:|:-:|
|  | ✅ | 0.1 | Simple |
| I/R | ❌ | .1 | Required integer digits. |
| F/R | ✅ | 1. | Required fraction digits. |
| E/R | ✅ | 1.0e | Required exponent digits. |
| M/R | ✅ | . | Required mantissa digits. |
| +/M | ❌ | +1.2 | No mantissa positive sign. |
| R/M | ❌ | 1.0 | Required positive sign. |
| e/e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R/E | ❌ | 1.0e3 | Required exponent sign. |
| e/F | ❌ | 1e3 | No exponent without fraction. |
| S/S | ✅ | NaN | No special (non-finite) values. |
| S/C | ✅ | nan | Case-sensitive special (non-finite) values. |
| N/F | ❌ | 001.2 | No float leading zeros. |
| R/e | ❌ | 1.2 | Required exponent notation. |
| e/C | ❌ | 1.0E3 | Case-sensitive exponent character. |
| I/E | ❌ | .1E3 | Require integer digits with exponent. |
| F/E | ✅ | 1.E3 | Require fraction digits with exponent. |
| r/P | ❌ | 0d1.2 | Require base prefixes. |
| r/S | ❌ | 1.2d | Require base suffixes. |
| M/E | ✅ | .e3 | Require mantissa digits with exponent. |
| I/I | ✅ | 1_1.11e11 | Integer internal digit separator. |
| F/I | ✅ | 11.1_1e11 | Fraction internal digit separator. |
| E/I | ✅ | 11.11e1_1 | Exponent internal digit separator. |
| I/L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F/L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E/L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I/T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F/T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E/T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I/C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F/C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E/C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S/D | ❌ | N_a_N | Special (non-finite) digit separator. |
| s/D | ❌ | _11.11e11 | Absolute start digit separator. |
| I/s | ❌ | _-11.11e11 | Integer sign digit separator. |
| I/c | ❌ | __-11.11e11 | Integer sign consecutive digit separator. |
| E/s | ❌ | 11.11e_-11 | Exponent sign digit separator. |
| E/c | ❌ | 11.11e__-11 | Exponent sign consecutive digit separator. |
| P/I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P/L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P/T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P/C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S/I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S/L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S/T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S/C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
|  | ✅ | 12 | Simple |
| N/I | ❌ | 0012 | No integer leading zeros. |
| e/P | ✅ | 0D12 | Case-sensitive base prefix. |
| e/S | ❌ | 12D | Case-sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |

## JSON

Parsing numbers via the JSON `Number` type(all are floats).Does not support base prefixes.

| Flag | Pass | Value | Title |
|: -:|: -:|: -:|: -:|
|  | ✅ | 0.1 | Simple |
| I / R | ✅ | .1 | Required integer digits. |
| F / R | ✅ | 1. | Required fraction digits. |
| E / R | ✅ | 1.0e | Required exponent digits. |
| M / R | ✅ | . | Required mantissa digits. |
| +/M | ✅ | +1.2 | No mantissa positive sign. |
| R / M | ❌ | 1.2 | Required positive sign. |
| e / e | ❌ | 1.0e3 | No exponent notation. |
| +/E | ❌ | 1.0e+3 | No exponent positive sign. |
| R / E | ❌ | 1.0e3 | Required exponent sign. |
| e / F | ❌ | 1e3 | No exponent without fraction. |
| S / S | ✅ | NaN | No special(non - finite) values. |
| S / C | ✅ | inf | Case - sensitive special(non - finite) values. |
| N / F | ✅ | 001.2 | No float leading zeros. |
| R / e | ❌ | 1.2 | Required exponent notation. |
| e / C | ❌ | 1.0E3 | Case - sensitive exponent character. |
| I / E | ✅ | .1E3 | Require integer digits with exponent. |
| F / E | ✅ | 1.E3 | Require fraction digits with exponent. |
| r / P | ❌ | 0d12 | Require base prefixes. |
| r / S | ❌ | 12d | Require base suffixes. |
| M / E | ✅ | .e3 | Require mantissa digits with exponent. |
| -/M | ❌ | -1.0 | No mantissa positive or negative sign. |
| -/E | ❌ | 1.0e-3 | No exponent positive or negative sign. |
| I / I | ❌ | 1_1.11e11 | Integer internal digit separator. |
| F / I | ❌ | 11.1_1e11 | Fraction internal digit separator. |
| E / I | ❌ | 11.11e1_1 | Exponent internal digit separator. |
| I / L | ❌ | -_11.11e11 | Integer leading digit separator. |
| F / L | ❌ | 11._11e11 | Fraction leading digit separator. |
| E / L | ❌ | 11.11e_11 | Exponent leading digit separator. |
| I / T | ❌ | 11_.11e11 | Integer trailing digit separator. |
| F / T | ❌ | 11.11_e11 | Fraction trailing digit separator. |
| E / T | ❌ | 11.11e11_ | Exponent trailing digit separator. |
| I / C | ❌ | 1__1.11e11 | Integer consecutive digit separator. |
| F / C | ❌ | 11.1__1e11 | Fraction consecutive digit separator. |
| E / C | ❌ | 11.11e1__1 | Exponent consecutive digit separator. |
| S / D | ❌ | N_a_N | Special(non - finite) digit separator. |
| s / D | ❌ | _11.11e11 | Absolute start digit separator. |
| I / s | ❌ | _ - 11.11e11 | Integer sign digit separator. |
| I / c | ❌ | __ - 11.11e11 | Integer sign consecutive digit separator. |
| E / s | ❌ | 11.11e_ - 11 | Exponent sign digit separator. |
| E / c | ❌ | 11.11e__ - 11 | Exponent sign consecutive digit separator. |
| P / I | ❌ | 0_d11.11e11 | Base prefix internal digit separator. |
| P / L | ❌ | -_0d11.11e11 | Base prefix leading digit separator. |
| P / T | ❌ | 0d_11.11e11 | Base prefix trailing digit separator. |
| P / C | ❌ | 0d__11.11e11 | Base prefix consecutive digit separator. |
| S / I | ❌ | 011.11e11d | Base suffix internal digit separator. |
| S / L | ❌ | 011.11e11_d | Base suffix leading digit separator. |
| S / T | ❌ | 011.11e11d_ | Base suffix trailing digit separator. |
| S / C | ❌ | 011.11e11d__ | Base suffix consecutive digit separator. |
| N / I | ✅ | 0012 | No integer leading zeros. |
| e / P | ❌ | 0D12 | Case - sensitive base prefix. |
| e / S | ❌ | 12D | Case - sensitive base suffix. |
| -/M | ❌ | -1 | No mantissa positive or negative sign. |
