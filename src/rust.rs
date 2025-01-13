pub fn main() {
    // DECIMAL - LITERAL
    // -----------------

    // FLAGS
    // I/R = Required integer digits.
    // E/R = Required exponent digits.
    // M/R = Required mantissa digits.
    // +/M = No mantissa positive sign.
    // S/S = No special (non-finite) values.
    // I/E = Require integer digits with exponent.
    // F/E = Require fraction digits with exponent.
    // M/E = Required mantissa digits with exponent.
    // p/I = The format supports parsing integers.
    // p/F = The format supports parsing floats.
    // w/I = The format supports writing integers.
    // w/F = The format supports writing floats.
    //
    // DIGIT SEPARATORS
    // I/I = Integer internal digit separator.
    // F/I = Fraction internal digit separator.
    // E/I = Exponent internal digit separator.
    // E/L = Exponent leading digit separator.
    // I/T = Integer trailing digit separator.
    // F/T = Fraction trailing digit separator.
    // E/T = Exponent trailing digit separator.
    // I/C = Integer consecutive digit separator.
    // F/C = Fraction consecutive digit separator.
    // E/C = Exponent consecutive digit separator.

    // literals - float
    let x: &[f64] = &[
        0.1,
        //.1,       // fails
        1.,
        //.,        // fails
        //1.e,      // fails
        //1.0e,     // fails
        //1.e3,     // fails
        1e3,
        1.0e3,
        1.0,
        //+1.0,     // fails
        1.0e3,
        //.e3       // fails
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

    // DECIMAL - STRINGS
    // -----------------

    // FLAGS
    // E/R = Required exponent digits.
    // M/R = Required mantissa digits.
    // M/E = Required mantissa digits with exponent.
    // p/I = The format supports parsing integers.
    // p/F = The format supports parsing floats.
    // w/I = The format supports writing integers.
    // w/F = The format supports writing floats.

    // string - floats
    let x: &[(&str, bool)] = &[
        ("0.1", true),
        (".1", true),
        ("1.", true),
        (".", false),
        ("1.e", false),
        ("1.0e", false),
        ("1.e3", true),
        ("1e3", true),
        ("1.0e3", true),
        ("1.0", true),
        ("+1.0", true),
        ("1.0e3", true),
        (".e3", false),
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

    // strings - integer
    let x: &[(&str, bool)] = &[
        ("1", true),
        ("+1", true),
        ("01", true),
        ("+01", true),
        ("_11", false),
        ("1_1", false),
        ("11_", false),
    ];
    for (i, s) in x {
        let r = i.parse::<i64>();
        println!("{i:#?}, {r:?}");
        assert_eq!(r.is_ok(), *s);
    }

    // HEX - LITERAL
    // -------------

    // FLAGS
    // I/R = Required integer digits.
    // +/M = No mantissa positive sign.
    // p/I = The format supports parsing integers.
    // w/I = The format supports writing integers.
    // e/P = Case-sensitive base prefix.
    // r/P = Require base prefixes.
    //
    // DIGIT SEPARATORS
    // I/I = Integer internal digit separator.
    // F/I = Fraction internal digit separator.
    // E/I = Exponent internal digit separator.
    // I/T = Integer trailing digit separator.
    // F/T = Fraction trailing digit separator.
    // E/T = Exponent trailing digit separator.
    // I/C = Integer consecutive digit separator.
    // F/C = Fraction consecutive digit separator.
    // E/C = Exponent consecutive digit separator.

    // literals - float
    // all hexadecimal floats are not supported
    let x: &[f64] = &[
        //0x1.0,    // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // literals - integers
    let x: &[i64] = &[
        //+0x1,    // fails
        -0x1,
        0x1,
        0x01,
        0x0_1,
        0x0__1,
        0x_01,
        0x__01,
        0x01_,
        0x01__,
        //0X01,     // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // BINARY - LITERAL
    // ----------------

    // FLAGS
    // I/R = Required integer digits.
    // +/M = No mantissa positive sign.
    // p/I = The format supports parsing integers.
    // w/I = The format supports writing integers.
    // e/P = Case-sensitive base prefix.
    // r/P = Require base prefixes.
    //
    // DIGIT SEPARATORS
    // I/I = Integer internal digit separator.
    // F/I = Fraction internal digit separator.
    // E/I = Exponent internal digit separator.
    // I/T = Integer trailing digit separator.
    // F/T = Fraction trailing digit separator.
    // E/T = Exponent trailing digit separator.
    // I/C = Integer consecutive digit separator.
    // F/C = Fraction consecutive digit separator.
    // E/C = Exponent consecutive digit separator.

    // literals - float
    // all binary floats are not supported
    let x: &[f64] = &[
        //0x1.0,    // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // literals - integers
    // all binary floats are not supported
    let x: &[i64] = &[
        //+0b1,    // fails
        -0b1,
        0b1,
        0b01
        0b0_1,
        0b0__1,
        0b_01,
        0b__01,
        0b01_,
        0b01__,
        //0B01,     // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // OCTAL - LITERAL
    // ---------------

    // FLAGS
    // I/R = Required integer digits.
    // +/M = No mantissa positive sign.
    // p/I = The format supports parsing integers.
    // w/I = The format supports writing integers.
    // e/P = Case-sensitive base prefix.
    // r/P = Require base prefixes.
    //
    // DIGIT SEPARATORS
    // I/I = Integer internal digit separator.
    // F/I = Fraction internal digit separator.
    // E/I = Exponent internal digit separator.
    // I/T = Integer trailing digit separator.
    // F/T = Fraction trailing digit separator.
    // E/T = Exponent trailing digit separator.
    // I/C = Integer consecutive digit separator.
    // F/C = Fraction consecutive digit separator.
    // E/C = Exponent consecutive digit separator.

    // literals - float
    // all binary floats are not supported
    let x: &[f64] = &[
        //0o1.0,    // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // literals - integers
    // all binary floats are not supported
    let x: &[i64] = &[
        //+0o1,    // fails
        -0o1,
        0o1,
        0o01,
        0o0_1,
        0o0__1,
        0o_01,
        0o__01,
        0o01_,
        0o01__,
        //0O01,     // fails
    ];
    for i in x {
        println!("{i:?}");
    }

    // NOTE That the string hex, binary, and octal values
    // are all basic formats, only support writing to, and
    // they alternate betweem required base prefixes and not
    // through the formatting API so we skip those.
    //
    // They can easy be built via the formatting API.
}
