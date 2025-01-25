package main

import (
    "log"
    "math"
)

func main() {{
    // NOTE: We use this to ignore the unused math import.
    // Go is terribly designed as a language at every level
    var _ float64 = math.NaN()

    var actual {type} = {value}
    var expected {type} = {expected}

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
