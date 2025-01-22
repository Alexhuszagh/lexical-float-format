# Rust - Decimal Literal

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
| M/E | ✅ | .1E3 | Require mantissa digits with exponent. |
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
