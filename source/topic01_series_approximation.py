"""Examples with using series to approximate functions.
"""


import numpy as np


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


if __name__ == "__main__":
    tol = 1e-8

    x = 0.
    if abs(np.exp(x) - exp(x)) < tol:
        print(f"Success for x = {x}.")
    else:
        print(f"Failed, expected : {np.exp(x)}, actual : {exp(x)}")

    x = 5.
    if abs(np.exp(x) - exp(x)) < tol:
        print(f"Success for x = {x}.")
    else:
        print(f"Failed, expected : {np.exp(x)}, actual : {exp(x)}")

    x = -5.
    if abs(np.exp(x) - exp(x)) < tol:
        print(f"Success for x = {x}.")
    else:
        print(f"Failed, expected : {np.exp(x)}, actual : {exp(x)}")

    print(f"e = {exp(1)}")
