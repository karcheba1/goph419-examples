"""Tests for series approximation example."""

import numpy as np

from topic01_series_approximation import (
        exp,
        )


def test_exp():
    """Tests for topic_01_series_approximation.exp()."""
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


if __name__ == '__main__':
    test_exp()
