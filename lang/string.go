package main

import (
    "strconv"
    "log"
    "math"
)

func ParseFloat(s string) (float64, error) {{
    f, err := strconv.ParseFloat(s, 64)
    return f, err
}}

func ParseInt(s string) (int64, error) {{
    i, err := strconv.ParseInt(s, {base}, 64)
    return i, err
}}

func ParseUint(s string) (uint64, error) {{
    i, err := strconv.ParseUint(s, {base}, 64)
    return i, err
}}

func main() {{
    // NOTE: We use this to ignore the unused math import.
    // Go is terribly designed as a language at every level
    var _ float64 = math.NaN()

    actual, err := {parse}("{value}")
    var expected {type} = {expected}

    if err != nil {{
        log.Fatalf("ParseError: %v", err)
    }}

    if expected != expected {{
        if actual == actual {{
            log.Fatal("AssertionError: actual == actual")
        }}
    }} else {{
        if actual != expected {{
            log.Fatal("AssertionError: `actual != expected`")
        }}
    }}
}}
