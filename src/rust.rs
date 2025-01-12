pub fn main() {
    // literals - float
    let x: &[f64] = &[
        0.1,
        //.1,       // fails
        1.,
        //.,        // fails
        //1.e,      // fails
        //1.0e,     // fails
        //1.e3,     // fails
        1.0e3,
        1.0,
        //+1.0,     // fails
        1.0e3,
        //.0e+3,    // fails
        //1.e+3,    // fails
        1.0e+3,
        1.0e3,
        01.0,
        1.0E3,
        1_1.11e11,
        11.1_1e11,
        11.11e1_1,
        //_11.11e11, // fails
        //11._11e11, // fails
        11.11e_11,
        11_.11e11,
        11.11_e11,
        11.11e11_,
        1__1.11e11,
        11.1__1e11,
        11.11e1__1,
        //NaN      // fails
        //nan      // fails
        //inf      // fails
        //Infinity // fails
        //na_n     // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // literals - integer
    let x: &[i64] = &[
        1,
        //+1,       // fails
        01,
        //+01,      // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // string - floats
    let x: &[(&str, bool)] = &[
        ("0.1", true),
        (".1", true),
        ("1.", true),
        (".", false),
        ("1.e", false),
        ("1.0e", false),
        ("1.e3", true),
        ("1.0e3", true),
        ("1.0", true),
        ("+1.0", true),
        ("1.0e3", true),
        (".0e+3", true),
        ("1.e+3", true),
        ("1.0e+3", true),
        ("1.0e3", true),
        ("01.0", true),
        ("1.0E3", true),
        ("1_1.11e11", false),
        ("11.1_1e11", false),
        ("11.11e1_1", false),
        ("_11.11e11", false),
        ("11._11e11", false),
        ("11.11e_11", false),
        ("11_.11e11", false),
        ("11.11_e11", false),
        ("11.11e11_", false),
        ("1__1.11e11", false),
        ("11.1__1e11", false),
        ("11.11e1__1", false),
        ("NaN", true),
        ("nan", true),
        ("inf", true),
        ("Inf", true),
        ("infinity", true),
        ("Infinity", true),
        ("na_n", false),
        ("infx", false),
    ];

    for (i, s) in x {
        let r = i.parse::<f64>();
        println!("{i:#?}, {r:?}");
        assert_eq!(r.is_ok(), *s);
    }

    // TODO: Add string formats
}
