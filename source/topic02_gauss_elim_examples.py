"""Some examples using Gauss elimination
and LU decomposition to solve linear systems.
"""

import numpy as np

from topic02_linalg_module import (
        gauss_naive_solve,
        )


def solve_1d_rhs_naive():
    """An example solving with a 1d rhs vector."""
    print("--------------------------------")
    print("Solve single RHS using naive GE:")
    print("--------------------------------\n")

    A = np.array([[60, 920, 160], [240, 40, 720], [700, 40, 120]])
    b = np.array([192, 720, 688])
    x = gauss_naive_solve(A, b)
    x_np = np.linalg.solve(A, b)

    print(f"A\n{A}\n")
    print(f"b\n{b}\n")
    print(f"x = gauss_naive_solve(A, b)\n{x}\n")
    print(f"x_np = numpy.linalg.solve(A, b)\n{x_np}\n")
    print(f"A * x\n{A @ x}")


if __name__ == "__main__":
    solve_1d_rhs_naive()
