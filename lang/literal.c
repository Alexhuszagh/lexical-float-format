#include <assert.h>
#include <math.h>
#include <stdint.h>

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
