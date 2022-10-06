"""Examples with using series to approximate functions.
"""


def exp(x):
    """Calculate the exponential function for real-valued input.

    Parameters
    ----------
    x : float
        The argument of the exponential function.

    Returns
    -------
    float
        The value of the exponential function.
    """
    eps_a = 1.
    eps_s = 1.e-16
    n = 0
    result = 0
    fact_n = 1
    while eps_a > eps_s:
        term = x**n / fact_n
        result += term
        n += 1
        fact_n *= n
        eps_a = abs(term / result)
    return result
