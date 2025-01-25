#include <assert.h>
#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

union number
{{
    int64_t i64;
    uint64_t u64;
    double f64;
}};

int64_t i64(const char* value) {{
    char* end;
    long i = strtol(value, &end, {base});
    if (*end != 0) {{
        printf("ParseError:\n");
        exit(1);
    }}
    return (int64_t)i;
}}

uint64_t u64(const char* value) {{
    char* end;
    unsigned long i = strtoul(value, &end, {base});
    if (*end != 0) {{
        printf("ParseError:\n");
        exit(1);
    }}
    return (uint64_t)i;
}}

double f64(const char *value) {{
    char* end;
    double f = strtod(value, &end);
    if (*end != 0) {{
        printf("ParseError:\n");
        exit(1);
    }}
    return f;
}}

int main() {{
    union number actual;
    union number expected;

    actual.{type} = {type}("{value}");
    expected.{type} = {expected};
    if (expected.{type} != expected.{type}) {{
        assert(actual.{type} != actual.{type});
    }} else {{
        assert(actual.{type} == expected.{type});
    }}
    return 0;
}}
