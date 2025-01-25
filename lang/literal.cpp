#include <cassert>
#include <cmath>
#include <stdint.h> // use for pre-C++11 compatability

typedef int64_t i64;
typedef uint64_t u64;
typedef double f64;

int main() {{
    {type} actual = {value};
    {type} expected = {expected};
    if (expected != expected) {{
        assert(actual != actual);
    }} else {{
        assert(actual == expected);
    }}
    return 0;
}}
