pub fn main() {{
    let x = "{value}".parse::<{type}>().unwrap();
    let expected: {type} = {expected};
    if expected != expected {{
        assert_eq!(x != x, true);
    }} else {{
        assert_eq!(x, expected);
    }}
}}
