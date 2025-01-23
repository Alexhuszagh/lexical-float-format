pub fn main() {{
    let x: {type} = {value};
    let expected: {type} = {expected};
    if expected != expected {{
        assert_eq!(x != x, true);
    }} else {{
        assert_eq!(x, expected);
    }}
}}
