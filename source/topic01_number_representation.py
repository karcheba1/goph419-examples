"""Examples related to number representation in different bases and types."""


def parse_sign(x):
    """Separate the sign and value of a number.

    Parameters
    ----------
    x : number
        The value to parse.

    Returns
    -------
    int
        The sign of the number.
        0 for +ve, 1 for -ve.
    number
        The absolute value of the number.
    """
    sign = 0
    if x < 0:
        sign = 1
        x = -x
    return sign, x


def max_power_int(x, base=2):
    """Determine the maximum power in a given base
    required to represent an integer.

    Parameters
    ----------
    x : int
        The integer to represent.
    base : int, optional, default=2
        The base in which to represent the integer.
        The default of 2 is for binary representation.

    Returns
    -------
    int
        The maximum place value power required
        to represent x in the given base.
    """
    n = 0
    while x >= base**n:     # >= guarantees the first digit will always be 0
        n += 1
    return n - 1            # now subtract 1 to avoid the leading 0


def normalize_float(x, base=2):
    """Get the normalized significand and exponent
    for a floating point value such that the significand
    is >= 1/base and < 1.

    Parameters
    ----------
    x : number
        The value to normalize.
    base : int, optional, default=2
        The base in which to represent the number.
        The default of 2 is for binary representation.

    Returns
    -------
    float
        The normalized significand.
    int
        The exponent after normalization.
    """
    e = 0
    min_value = 1 / base
    while x < min_value:
        x *= base
        e -= 1
    while x >= 1.0:
        x /= base
        e += 1
    return x, e


def digit_list(x, max_pow, min_pow=0, base=2):
    """Get a list of digits representing a number
    to a place value power
    in a given base.

    Parameters
    ----------
    x : number
        The value to decompose.
    max_pow : int
        Maximum place value power.
    min_pow : int, optional, default=0
        Minimum place value power.
        The default value of 0 works for integers, but not for floats.
    base : int, optional, default=2
        The base in which to represent the number.
        The default value of 2 is for binary representation.

    Returns
    -------
    list
        A list of digit place values.
        The values may not correspond to single digits,
        so it may be necessary to convert them for base>10.
    """
    result = []
    n = max_pow
    while n >= min_pow:
        if x >= base**n:    # in this case, there is a non-zero digit
            result.append(int(x // base**n))    # calculate the digit
            x %= base**n  # get the remainder that still needs to be stored
        else:
            result.append(0)
        n -= 1
    return result


def digits_to_str_int(x, sign, digit_dict=None):
    """Convert a list of integer digits to a string.

    Parameters
    ----------
    x : list
        The list of digits to convert.
    sign : int
        The sign digit.
    digit_dict : dict, optional
        A dict for converting digit values to single digit strings.

    Returns
    -------
    str
        The string representation of the input list.
    """
    # convert digits to string, optionally use a dict to convert digits
    if digit_dict:
        result = [str(digit_dict[d]) for d in x]
    else:
        result = [str(d) for d in x]
    result.insert(0, " ")   # insert a space between sign and digits
    result.insert(0, str(sign)) # insert the sign bit
    return "".join(result)  # concatenate the digits together without spaces


def decimal_string_int(x):
    """Represent a number as an integer decimal string.

    Parameters
    ----------
    x : int
        A number to convert to decimal representation.
        Could take a variety of formats:
        int, binary int, hexadecimal int, float

    Returns
    -------
    str
        Decimal string representation of the integer.

    Notes
    -----
    An attempt is made to cast the input with int().
    For float input, this will result in chopping of fractional amounts.
    """
    x = int(x)  # attempt to cast to int, so we can assume this later
    sign, x = parse_sign(x)
    n = max_power_int(x, base=10)
    return digits_to_str_int(digit_list(x, n, base=10), sign)


def binary_string_int(x):
    """Represent a number as an integer binary string.

    Parameters
    ----------
    x : int
        A number to convert to binary representation.
        Could take a variety of formats:
        int, binary int, hexadecimal int, float

    Returns
    -------
    str
        Binary string representation of the integer.

    Notes
    -----
    An attempt is made to cast the input with int().
    For float input, this will result in chopping of fractional amounts.
    """
    x = int(x)  # attempt to cast to int, so we can assume this later
    sign, x = parse_sign(x)
    n = max_power_int(x)
    return digits_to_str_int(digit_list(x, n), sign)


def binary_string_float64(x):
    """Represent a non-integer number as a binary string.
    Uses IEEE-754 double precision (64-bit) format.

    Parameters
    ----------
    x : float
        A number to convert to binary representation.

    Returns
    -------
    str
        Binary string representation of the number.

    Notes
    -----
    An attempt is made to cast the input with float().
    """
    x = float(x)  # attempt to cast to float, so we can assume this later
    sign, x = parse_sign(x)     # split sign and value of the number
    x, e = normalize_float(x)   # get significand and exponent
    e_sign, e = parse_sign(e)   # split sign and value of exponent
    # get exponent str, 2**9 is max place value for double precision
    e_str = digits_to_str_int(digit_list(e, max_pow=9), e_sign)
    result = digit_list(x, -1, -53)     # get digits of significand
    # convert significand to string representation
    # sign bit, then exponent bits, then significand bits
    return "".join([str(sign),
                    " ", e_str,
                    " ", "".join([str(d) for d in result])])


def main():
    print("\nConverting numbers to decimal and binary representation:")

    x = 173
    print(f"\nx : {x}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")

    x = -173
    print(f"\nx : {x}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")

    x = 0b001001  # 9 in binary, the 0b prefix tells Python it is binary
    print(f"\nx : {bin(x)}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")

    x = 0o0011  # 9 in octal, the 0o prefix tells Python it is octal
    print(f"\nx : {oct(x)}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")

    x = -0x1f   # -31 in hexadecimal (base-16), 1*16**1 + 15*16**0
    # note: hexadecimal has digits: 0-9, a-f to represent 15 place values
    print(f"\nx : {hex(x)}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")

    x = 12.867  # float input
    print(f"\nx : {x}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")

    x = 1.567
    print(f"\nx : {x}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")

    x = 0.2
    print(f"\nx : {x}")
    print(f"dec : {decimal_string_int(x)}")
    print(f"bin : {binary_string_int(x)}")
    print(f"float : {binary_string_float64(x)}")


if __name__ == "__main__":
    main()
