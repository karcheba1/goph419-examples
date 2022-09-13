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


def main():
    print("\nConverting numbers to decimal representation:")
    x = 173
    print(f"x : {x:6}, dec : {decimal_string_int(x)}")
    x = -173
    print(f"x : {x:6}, dec : {decimal_string_int(x)}")
    x = 0b001001  # 9 in binary, the 0b prefix tells Python it is binary
    print(f"x : {bin(x):6}, dec : {decimal_string_int(x)}")
    x = 0o0011  # 9 in octal, the 0o prefix tells Python it is octal
    print(f"x : {oct(x):6}, dec : {decimal_string_int(x)}")
    x = -0x1f   # -31 in hexadecimal (base-16), 1*16**1 + 15*16**0
    # note: hexadecimal has digits: 0-9, a-f to represent 15 place values
    print(f"x : {hex(x):6}, dec : {decimal_string_int(x)}")


if __name__ == "__main__":
    main()
