trait IsNan {{
    fn is_nan(&self) -> bool {{
        false
    }}
}}

impl IsNan for i64 {{
}}

pub fn main() {{
    let x: {type} = {value};
    let expected: {type} = {expected};
    if expected.is_nan() {{
        assert_eq!(x.is_nan(), expected.is_nan());
    }} else {{
        assert_eq!(x, expected);
    }}
}}
