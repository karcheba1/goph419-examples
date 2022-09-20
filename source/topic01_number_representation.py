"""Examples related to number representation in different bases and types."""


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
    # store the sign, so we can assume positive values later
    sign = 0  # 0 for +ve, 1 for -ve
    if x < 0:
        sign = 1
        x = -x
    # find the maximum digit
    # using >= here guarantees the first bit will always be 0
    # then we can pop it later, and replace it with the sign bit
    n = 0
    while x >= 10**n:
        n += 1
    # store the value as a list of digits
    result = []
    while n >= 0:
        if x >= 10**n:
            result.append(x // 10**n)
            x %= 10**n  # get the remainder that still needs to be stored
        else:
            result.append(0)
        n -= 1
    # convert to string representation
    result.pop(0)
    result = [str(d) for d in result]
    result.insert(0, " ")
    result.insert(0, str(sign))
    return "".join(result)


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
    # store the sign, so we can assume positive values later
    sign = 0  # 0 for +ve, 1 for -ve
    if x < 0:
        sign = 1
        x = -x
    # find the maximum digit
    # using >= here guarantees the first bit will always be 0
    # then we can pop it later, and replace it with the sign bit
    n = 0
    b = 2
    while x >= b**n:
        n += 1
    # store the value as a list of bits
    result = []
    while n >= 0:
        if x >= b**n:
            result.append(1)
            x -= b**n  # get the remainder that still needs to be stored
        else:
            result.append(0)
        n -= 1
    # convert to string representation
    result.pop(0)
    result = [str(d) for d in result]
    result.insert(0, " ")
    result.insert(0, str(sign))
    return "".join(result)


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
    # store the sign, so we can assume positive values later
    sign = 0  # 0 for +ve, 1 for -ve
    if x < 0:
        sign = 1
        x = -x
    # normalize the significand / find the exponent
    e = 0
    while x >= 1.0:
        x /= 2
        e += 1
    while x < 0.5:
        x *= 2
        e -= 1
    # store the exponent as a list of bits
    e_sign = 0
    if e < 0:
        e_sign = 1
        e = -e
    result = []
    n = 9       # maximum exponent bit for double precision
    while n >= 0:
        if e >= 2**n:
            result.append(1)
            e -= 2**n  # get the remainder that still needs to be stored
        else:
            result.append(0)
        n -= 1
    # convert to string representation
    result = [str(d) for d in result]
    result.insert(0, " ")
    result.insert(0, str(e_sign))
    e_str = "".join(result)
    # calculate bits of the significand
    result = []
    N = 53       # minimum significand bit for double precision
    while n >= -N:
        if x >= 2**n:
            result.append(1)
            x -= 2**n  # get the remainder that still needs to be stored
        else:
            result.append(0)
        n -= 1
    # convert significand to string representation
    result = [str(d) for d in result]
    return "".join([str(sign), " ", e_str, " ", "".join(result)])


def main():
    print("\nConverting numbers to decimal and binary representation:")
    x = 173
    print(f"x : {x:6}, dec : {decimal_string_int(x)}")
    print(f"x : {x:6}, bin : {binary_string_int(x)}")
    print(f"x : {x:6}, float : {binary_string_float64(x)}")
    x = -173
    print(f"x : {x:6}, dec : {decimal_string_int(x)}")
    print(f"x : {x:6}, bin : {binary_string_int(x)}")
    x = 0b001001  # 9 in binary, the 0b prefix tells Python it is binary
    print(f"x : {bin(x):6}, dec : {decimal_string_int(x)}")
    print(f"x : {bin(x):6}, bin : {binary_string_int(x)}")
    x = 0o0011  # 9 in octal, the 0o prefix tells Python it is octal
    print(f"x : {oct(x):6}, dec : {decimal_string_int(x)}")
    print(f"x : {oct(x):6}, bin : {binary_string_int(x)}")
    x = -0x1f   # -31 in hexadecimal (base-16), 1*16**1 + 15*16**0
    # note: hexadecimal has digits: 0-9, a-f to represent 15 place values
    print(f"x : {hex(x):6}, dec : {decimal_string_int(x)}")
    print(f"x : {hex(x):6}, bin : {binary_string_int(x)}")
    x = 12.867  # float input
    print(f"x : {x:6}, dec : {decimal_string_int(x)}")
    print(f"x : {x:6}, bin : {binary_string_int(x)}")
    x = 1.567
    print(f"x : {x:6}, float : {binary_string_float64(x)}")


if __name__ == "__main__":
    main()
