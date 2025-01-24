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
