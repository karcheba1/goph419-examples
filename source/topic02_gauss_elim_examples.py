"""Some examples using Gauss elimination
and LU decomposition to solve linear systems.
"""

import numpy as np

from topic02_linalg_module import (
        gauss_solve,
        )


def solve_1d_rhs_naive():
    """An example solving with a 1d rhs vector using naive GE."""

    print("\n--------------------------------")
    print("Solve single RHS using naive GE:")
    print("--------------------------------\n")

    A = np.array([[60, 920, 160], [240, 40, 720], [700, 40, 120]])
    b = np.array([192, 720, 688])
    x = gauss_solve(A, b, pivot=False)[0]
    x_np = np.linalg.solve(A, b)

    print(f"A\n{A}\n")
    print(f"b\n{b}\n")
    print(f"x = gauss_solve(A, b, pivot=False)[0]\n{x}\n")
    print(f"x_np = numpy.linalg.solve(A, b)\n{x_np}\n")
    print(f"A @ x\n{A @ x}")


def solve_Ainv_naive():
    """An example solving for a matrix inverse using naive GE."""

    print("\n--------------------------------")
    print("Solve Ainv using naive GE:")
    print("--------------------------------\n")

    A = np.array([[60, 920, 160], [240, 40, 720], [700, 40, 120]])
    Ainv = gauss_solve(A, np.eye(A.shape[0]), pivot=False)[0]

    print(f"A\n{A}\n")
    print("Ainv = gauss_solve(A, numpy.eye(A.shape[0]), pivot=False)[0]"
          + f"\n{Ainv}\n")
    print(f"A @ Ainv\n{A @ Ainv}")


def solve_1d_rhs_pivot():
    """An example solving with a 1d rhs vector."""

    print("\n--------------------------------")
    print("Solve single RHS using GE with partial pivoting:")
    print("--------------------------------\n")

    A = np.array([[60, 920, 160], [240, 40, 720], [700, 40, 120]])
    b = np.array([192, 720, 688])
    x = gauss_solve(A, b)[0]
    x_np = np.linalg.solve(A, b)

    print(f"A\n{A}\n")
    print(f"b\n{b}\n")
    print(f"x = gauss_solve(A, b)[0]\n{x}\n")
    print(f"x_np = numpy.linalg.solve(A, b)\n{x_np}\n")
    print(f"A @ x\n{A @ x}")


def solve_Ainv_pivot():
    """An example solving for a matrix inverse using GE
    with partial pivoting.
    """

    print("\n--------------------------------")
    print("Solve Ainv using GE with partial pivoting:")
    print("--------------------------------\n")

    A = np.array([[60, 920, 160], [240, 40, 720], [700, 40, 120]])
    Ainv = gauss_solve(A, np.eye(A.shape[0]))[0]

    print(f"A\n{A}\n")
    print("Ainv = gauss_solve(A, numpy.eye(A.shape[0]))[0]"
          + f"\n{Ainv}\n")
    print(f"A @ Ainv\n{A @ Ainv}")


def get_LU_decomp_combined():
    """An example solving for the LU decomposition of a matrix using GE
    with partial pivoting.
    """

    print("\n--------------------------------")
    print("Solve for LU and P using GE with partial pivoting:")
    print("--------------------------------\n")

    A = np.array([[60, 920, 160], [240, 40, 720], [700, 40, 120]])
    LU, P = gauss_solve(A, np.empty((A.shape[0], 1)))[1:]
    L_times_U = (np.tril(LU, -1) + np.eye(A.shape[0])) @ np.triu(LU)

    print(f"A\n{A}\n")
    print("LU, P = gauss_solve(A, numpy.empty((A.shape[0], 1)))[1:]"
          + f"\n\nLU\n{LU}\n\nP\n{P}")
    print(f"\nL @ U\n{L_times_U}")
    print(f"\nP @ A\n{P @ A}")


def get_LU_decomp_split():
    """An example solving for the LU decomposition of a matrix using GE
    with partial pivoting.
    """

    print("\n--------------------------------")
    print("Solve for L, U, and P using GE with partial pivoting:")
    print("--------------------------------\n")

    A = np.array([[60, 920, 160], [240, 40, 720], [700, 40, 120]])
    (L, U), P = gauss_solve(A, np.empty((A.shape[0], 1)), split_LU=True)[1:]

    print(f"A\n{A}\n")
    print("(L, U), P = gauss_solve(A, numpy.empty((A.shape[0], 1)), "
          + "split_LU=True)[1:]"
          + f"\n\nL\n{L}\n\nU\n{U}\n\nP\n{P}")
    print(f"\nL @ U\n{L @ U}")
    print(f"\nP @ A\n{P @ A}")
    print(f"\nP.T @ L @ U\n{P.T @ L @ U}")


if __name__ == "__main__":
    solve_1d_rhs_naive()
    solve_Ainv_naive()
    solve_1d_rhs_pivot()
    solve_Ainv_pivot()
    get_LU_decomp_combined()
    get_LU_decomp_split()
