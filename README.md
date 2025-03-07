# float format

This contains scripts and code to determine the valid float parsing formats for both literals and parsing from string for a large number of programming languages for inclusion in [prebuilt_formats](https://github.com/Alexhuszagh/rust-lexical/blob/main/lexical-util/src/prebuilt_formats.rs). This requires many different compilers and compiler versions, as well as a large number of test cases for each.

For each test, if it supports custom hex strings, the special strings, or similar, you should comment each at the top.

## Toolchains

1. [Rust](https://rustup.rs/)
2. [Python](https://www.python.org/downloads/)
3. [C/C++](https://gcc.gnu.org/)
4. [Julia](https://julialang.org/)
5. [Go](https://go.dev/)
6. [Elm](https://elm-lang.org/)
7. [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
8. [Ruby](https://www.ruby-lang.org/en/)
9. [Elixir](https://elixir-lang.org/)
10. [Scala](https://www.scala-lang.org/)
11. [Haskell](https://www.haskell.org/ghc/)
12. [Perl](https://www.perl.org/)
13. [PHP](https://www.php.net/)
14. [Kotlin](https://kotlinlang.org/)
15. [R](https://www.r-project.org/)
16. [Gambit-C](https://gambitscheme.org/)
17. [Guile](https://www.gnu.org/software/guile/)
18. [Clojure](https://clojure.org/)
19. [Erlang](https://www.erlang.org/)
20. [FORTRAN](https://fortran-lang.org/)
21. [D](https://dlang.org/)
22. [CoffeeScript](https://coffeescript.org/)
23. [COBOL](https://www.ibm.com/think/topics/cobol)
24. [Flutter](https://flutter.dev/)
25. [.NET](https://learn.microsoft.com/en-us/dotnet/)
26. [OCaml](https://ocaml.org/)
27. [Objective-C](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html)
28. [ReasonML](https://reasonml.github.io/)
29. [Zig](https://ziglang.org)
30. [Octave](https://octave.org/) (and MATLAB)
31. [SageMath](https://www.sagemath.org/)
32. [Java](https://www.java.com/en/)
33. [Pascal](https://www.lazarus-ide.org/)
34. [Lua](https://www.lua.org/)
35. [Groovy](https://groovy-lang.org/)
36. [Lisp](https://lisp-lang.org/)
37. [ADA](https://ada-lang.io/)
38. [Nim](https://nim-lang.org/)
39. [Crystal](https://crystal-lang.org/)
40. [Swift](https://www.swift.org/)

On Ubuntu, these toolchains can be installed as follows:

```bash
sudo apt install -y \
    elm-compiler \
    gcc g++ \
    python3 python-is-python3 \
    golang-go \
    nodejs \
    ruby \
    elixir \
    scala \
    ghc \
    php-cli \
    kotlin \
    r-base-core \
    gambc \
    guile-3.0 \
    clojure \
    coffeescript \
    gnucobol3 \
    dotnet-host-8.0 dotnet-sdk-8.0 \
    ocaml opam \
    gobjc \
    octave \
    gdebi \
    lua5.4 \
    groovy \
    sbcl \
    alire \
    nim \
    crystal

sudo snap install julia --classic
sudo snap install dmd --classic
sudo snap install flutter --classic
sudo snap install --beta zig --classic

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

opam init
opam install reason

# Swift is a pain
curl https://download.swift.org/swift-6.0.3-release/ubuntu2404/swift-6.0.3-RELEASE/swift-6.0.3-RELEASE-ubuntu24.04.tar.gz
mv swift-6.0.3-RELEASE-ubuntu24.04.tar.gz ~/Downloads
tar xvf ~/Downloads/swift-6.0.3-RELEASE-ubuntu24.04.tar.gz -C ~/Downloads/
mv ~/Downloads/swift-6.0.3-RELEASE-ubuntu24.04 ~/Downloads/swift
```

## Running Tests

The main test case is in [run.sh](/scripts/run.sh), but each individual test can easily be extracted from there.

## Test Cases

The main test cases are:
1. `.1` - required_integer_digits
2. `1.` - required_fraction_digits
3. `1.0e` - required_exponent_digits
4. `.` - required_mantissa_digits
5. `+1` - no_positive_mantissa_sign
6. `1` - required_mantissa_sign
7. `1.0e3` - no_exponent_notation
8. `1.0e+3` - no_positive_exponent_sign
9. `1.0e3` - required_exponent_sign
10. `1e3` - no_exponent_without_fraction
11. `1.e3` - required_integer_digits_with_exponent
12. `.1e3` - required_fraction_digits_with_exponent
13. `.e3` - required_mantissa_digits_with_exponent
14. `01` - no_integer_leading_zeros
15. `01.0` - no_float_leading_zeros
16. `1.0` - required_exponent_notation
17. `1.0E3` - case_sensitive_exponent
18. `1_1.11e11` - integer_internal_digit_separator
19. `1_1.11e11` - mantissa_internal_digit_separator (TODO: Add the flag name)
20. `11.1_1e11` - fraction_internal_digit_separator
21. `11.11e1_1` - exponent_internal_digit_separator
22. `_11.11e11` - integer_leading_digit_separator
23. `_11.11e11` - mantissa_leading_digit_separator (TODO: Add the flag name)
24. `11._11e11` - fraction_leading_digit_separator
25. `11.11e_11` - exponent_leading_digit_separator
26. `11_.11e11` - integer_trailing_digit_separator
27. `11_.11e11` - mantissa_trailing_digit_separator (TODO: Add the flag name)
28. `11.11_e11` - fraction_trailing_digit_separator
29. `11.11e11_` - exponent_trailing_digit_separator
30. `1__1.11e11` - integer_consecutive_digit_separator
31. `1__1.11e11` - mantissa_consecutive_digit_separator (TODO: Add the flag name)
32. `11.1__1e11` - fraction_consecutive_digit_separator
33. `11.11e1__1` - exponent_consecutive_digit_separator
34. `_`, `_.1` - Digit separator with empty integer
35. `__`, `__.1` - Consecutive digit separator with empty integer
36. `1._` - Digit separator with empty fraction
37. `1.__` - Consecutive digit separator with empty fraction
38. `_._` - Digit separator with empty mantissa
39. `__.__` -  Consecutive digit separator with empty mantissa
40. `1.2e_` - Digit separator with empty exponent
41. `1.2e__` - Consecutive digit separator with empty exponent

Test cases that might depend on the specific string representations of special numbers include:
42. `NaN` - no_special
43. `nan` - case_sensitive_special
44. `na_n` - special_digit_separator
45. `na__n` - Consecutive special digit separator. (TODO: Change to have flag name)
46. `NaN` - NaN is supported (TODO: Change to have flag name)
47. `++NaN` - Allows a positive sign before a representation of NaN. (TODO: Change to have flag name)
48. `-NaN` - Allows a negative sign before a representation of NaN. (TODO: Change to have flag name)
49. `NaN` - Has a case-sensitive representation of NaN. (TODO: Change to have flag name)
50. `Inf` - Short infinity representation is supported. (TODO: Change to have flag name)
51. `+Inf` - Allows a positive sign before a representation of short infinity. (TODO: Change to have flag name)
52. `-Inf` - Allows a negative sign before a representation of short infinity. (TODO: Change to have flag name)
53. `Inf` - Has a case-sensitive representation of short infinity. (TODO: Change to have flag name)
54. `Infinity` - Long infinity representation is supported (TODO: Change to have flag name)
55. `+Infinity` - Allows a positive sign before a representation of long infinity. (TODO: Change to have flag name)
56. `-Infinity` - Allows a negative sign before a representation of long infinity. (TODO: Change to have flag name)
57. `Infinity` - Has a case-sensitive representation of long infinity. (TODO: Change to have flag name)

Test cases that might depend on radix support and more include:
58. `0x1` - Supports base prefixes (TODO: Change to have flag name)
59. `0x1` - Does not support base prefixes (TODO: Change to have flag name)
60. `0X1` - case_sensitive_base_prefix
61. `1` - required_base_prefix
62. `1h` - Supports base suffixes (TODO: Change to have flag name)
63. `1h` - Does not supports base suffixes (TODO: Change to have flag name)
64. `1H` - case_sensitive_base_suffix
65. `1` - required_base_suffix
66. `-0_x1` - base_prefix_internal_digit_separator
67. `-_0x1` - base_prefix_leading_digit_separator
68. `-0x_1` - base_prefix_trailing_digit_separator (overlaps with leading integer/mantissa digit separator)
69. `0x__1` - base_prefix_consecutive_digit_separator
70. `1h` - base_suffix_internal_digit_separator (can never occur, future-proofing)
71. `1_h` - base_suffix_leading_digit_separator (overlaps with trailing integer/mantissa/exponent digit separator)
72. `1h_` - base_suffix_trailing_digit_separator
73. `1h__` - base_suffix_consecutive_digit_separator

Additional format feature test cases:
74. `-0`: no_unsigned_negative_sign
75. `-0.0`: no_mantissa_negative_sign
76. `-0`: no_exponent_negative_sign
77. `_1`: start_digit_separator
78. `_+1`: integer_sign_digit_separator
79. `__+1`: integer_consecutive_sign_digit_separator
80. `_+1`: mantissa_sign_digit_separator (TODO: Change to have flag name)
81. `__+1`: mantissa_consecutive_sign_digit_separator (TODO: Change to have flag name)
82. `1.0e_+1`: exponent_sign_digit_separator
83. `1.0e__+1`: exponent_consecutive_sign_digit_separator

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
