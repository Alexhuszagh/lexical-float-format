# float format

This contains scripts and code to determine the valid float parsing formats for both literals and parsing from string for a large number of programming languages for inclusion in [prebuilt_formats](https://github.com/Alexhuszagh/rust-lexical/blob/main/lexical-util/src/prebuilt_formats.rs). This requires many different compilers and compiler versions, as well as a large number of test cases for each.

For each test, if it supports custom hex strings, the special strings, or similar, you should comment each at the top.

## Toolchains

1. [Rust](https://rustup.rs/)
2. [Python](https://www.python.org/downloads/)
3. [C#](https://dotnet.microsoft.com/en-us/download)

## Running Tests

The main test case is in [run.sh](/scripts/run.sh), but each individual test can easily be extracted from there.

## Test Cases

The main test cases are:
- `.1` - required_integer_digits
- `1.` - required_fraction_digits
- `1.0e` - required_exponent_digits
- `.` - required_mantissa_digits
- `+1` - no_positive_mantissa_sign
- `1` - required_mantissa_sign
- `1.0e3` - no_exponent_notation
- `1.0e+3` - no_positive_exponent_sign
- `1.0e3` - required_exponent_sign
- `1e3` - no_exponent_without_fraction
- `1.e3` - required_integer_digits_with_exponent
- `.1e3` - required_fraction_digits_with_exponent
- `.e3` - required_mantissa_digits_with_exponent
- `01` - no_integer_leading_zeros
- `01.0` - no_float_leading_zeros
- `1.0` - required_exponent_notation
- `1.0E3` - case_sensitive_exponent
- `1_1.11e11` - integer_internal_digit_separator
- `11.1_1e11` - fraction_internal_digit_separator
- `11.11e1_1` - exponent_internal_digit_separator
- `_11.11e11` - integer_leading_digit_separator
- `11._11e11` - fraction_leading_digit_separator
- `11.11e_11` - exponent_leading_digit_separator
- `11_.11e11` - integer_trailing_digit_separator
- `11.11_e11` - fraction_trailing_digit_separator
- `11.11e11_` - exponent_trailing_digit_separator
- `1__1.11e11` - integer_consecutive_digit_separator
- `11.1__1e11` - fraction_consecutive_digit_separator
- `11.11e1__1` - exponent_consecutive_digit_separator

Test cases that might depend on the specific string representations of special numbers include:
- `NaN` - no_special
- `nan` - case_sensitive_special
- `na_n` - special_digit_separator

Test cases that might depend on radix support and more include:
- base_prefix
- base_suffix
- case_sensitive_base_prefix
- case_sensitive_base_suffix
- required_base_prefix
- required_base_suffix

## Test Data Format

We use a TOML data format for each language, which dictates the runner and type for the tests so new float formats can be added with minimal effort. The format, along with the defaults are below. The 3 top-level keys supported are:
- metadata
- floats
- integers

```toml
[metadata]
# the title to print when running the test
# the {} is a placeholder for the version
title = "Rust - Decimal Literal - {version}"
# can be a literal or a string
literal = true
# the programming language to use
language = "rust"
# An optional radix for the number (defaults to 10)
base = 10

[[floats]]
# the value to test (required)
value = "0.1"
# the title for the test (required)
title = "Simple"
# short-hand flags when writing a table (optional)
flags = ""
# if the format is supported if the test passes or fails
# the valid values are "pass" and "fail". defaults to "pass"
outcome = "pass"

[[floats]]
# the value to test (required)
value = ".1"
# the title for the test (required)
title = "Required integer digits."
# short-hand flags when writing a table (optional)
flags = "I/R"
outcome = "pass"

[[ints]]
# the value to test (required)
value = ".1"
# the title for the test (required)
title = "Required integer digits."
# short-hand flags when writing a table (optional)
flags = "I/R"
outcome = "pass"
```

`value` can be either a value or an array of values, in which case of an array, will check that all have the same result or an error will occur, notifying that more complex logic is required.

Additional settings, such as language compiler versions and lang versions can be specified such as in [config.toml](/config.toml).
