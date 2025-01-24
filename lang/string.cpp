#include <cassert>
#include <cstdlib>

union number
{{
    int i32;
    unsigned int u32;
    double f64;
}};

int i32(const char* value) {{
    char* end;
    int i = std::strtol(value, &end, {base});
    if (*end != 0) {{
        assert(false);
    }}
    return i;
}}

unsigned int u32(const char* value) {{
    char* end;
    unsigned int i = strtoul(value, &end, {base});
    if (*end != 0) {{
        assert(0);
    }}
    return i;
}}

double f64(const char *value) {{
    char* end;
    double f = std::strtod(value, &end);
    if (*end != 0) {{
        assert(false);
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
