"""An example module containing Gauss elimination
and related routines.
"""


import numpy as np


def _validate_gauss_input(A, b):
    # make sure that A and b are array_like of float
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    # check that A is 2d
    # note the use of the := operator within expressions
    # to define / assign values to variables we may want
    # to use again later
    if (ndimA := len(A.shape)) != 2:
        raise ValueError(f"A is {ndimA}-dimensional, should be 2d")
    # check that A is square
    if not (n := A.shape[0]) == (m := A.shape[1]):
        raise ValueError(f"A has {n} rows and {m} columns, should be square")
    # check that b is 1d or 2d
    if (ndimb := len(b.shape)) not in [1, 2]:
        raise ValueError(f"b is {ndimb}-dimensional, should be 1d or 2d")
    # check that b has same number of rows as A
    if (mb := b.shape[0]) != n:
        raise ValueError(f"A has {n} rows and b has {mb} rows, "
                         + "should be equal")
    # reshape b if 1d, set flag for output return format
    if out_1d := (len(b.shape) == 1):
        b = np.reshape(b, (n, nb := 1))
    else:
        nb = b.shape[1]
    # return the validated input and properties
    return A, b, n, nb, out_1d


def _form_augmented_matrix(A, b):
    """Form an augmented matrix from a coefficient matrix A
    and a rhs matrix b.

    Parameters
    ----------
    A : array_like, shape = (n, n)
        The coefficient matrix
    b : array_like, shape = (n, nb), nb >= 1
        The right-hand-side matrix

    Returns
    -------
    numpy.ndarray
        The augmented matrix with A on the left and b on the right

    Notes
    -----
    Does not explicitly check for compatible dimensions of A and b.
    """
    return np.hstack([A, b])


def _forward_elimination(A, n, pivot=True):
    """Perform forward elimination on a matrix.

    Parameters
    ----------
    A : numpy.ndarray, shape = (n, m), m >= n
        A coefficient or augmented matrix
    n : int
        The number of rows in A

    Returns
    -------
    numpy.ndarray
        The reduced matrix, with elimination coefficients in lower triangle

    Notes
    -----
    Does not explicitly check that A.shape[0] == n
    """
    m = A.shape[1]
    if pivot:
        Ae = np.hstack([A, np.eye(n)])  # initialize permutation matrix
    else:
        Ae = np.array(A) # make a copy, do not overwrite A
    k = 0
    while (kp1 := k + 1) < n:
        if pivot:
            # get absolute values of coefficients at and below the pivot
            A_abs_piv = np.abs(Ae[k:, k])
            piv_max = np.max(A_abs_piv)
            # get the index of the row with the maximum pivot value
            kmax = np.nonzero(A_abs_piv == piv_max)[0][0] + k
            # swap rows, if necessary
            if kmax != k:
                Ae[k, :], Ae[kmax, :] = Ae[kmax, :].copy(), Ae[k, :].copy()
        # compute elimination coefficients
        Ae[kp1:m, k] /= Ae[k, k]
        # eliminate below the pivot
        Ae[kp1:, kp1:m] -= Ae[kp1:, k:kp1] @ Ae[k:kp1, kp1:m]
        # increment pivot index
        k += 1
    return Ae[:, :m]


def _backward_substitution(A, n):
    """Perform backward substitution on an augmented matrix.

    Parameters
    ----------
    A : numpy.ndarray, shape = (n, m), m > n
        The augmented matrix in reduced (upper triangular) form
    n : int
        The number of rows in A

    Returns
    -------
    numpy.ndarray
        The augmented matrix after performing backward substitution.
        The solution is in columns [n:].

    Notes
    -----
    Does not explicitly check that A.shape[0] == n
    """
    Ab = np.array(A) # make a copy, do not overwrite A
    k = n - 1
    while (kp1 := k + 1) > 0:
        if kp1 < n:
            Ab[k:kp1, n:] -= Ab[k:kp1, kp1:n] @ Ab[kp1:n, n:]
        Ab[k:kp1, n:] /= Ab[k, k]
        k -= 1
    return Ab


def gauss_solve(A, b, pivot=True):
    """Solve a system A * x = b for x using Gaussian elimination.

    Parameters
    ----------
    A : array_like, shape = (n, n)
        The coefficient matrix
    b : array_like, shape = (n, *)
        The right-hand-side vector(s)
    pivot : bool, optional, default=True
        Flag for performing partial pivoting

    Returns
    -------
    numpy.ndarray, shape = (n, *)
        The solution to the system, same shape as b

    Raises
    ------
    ValueError
        If A is not 2d and square
        If b is not 1d or 2d, or has a different number of rows from A

    Notes
    -----
    If pivot == False, performs naive Gaussian elimination
    with no pivoting.
    If pivot == True, performs Gaussian elimination
    with partial pivoting (pivot rows, but not columns).
    In either case, it may fail due to divide-by-zero in a pivot position
    even when A is not singular.
    This is less common when pivot == True (the default).
    """
    A, b, n, nb, out_1d = _validate_gauss_input(A, b)
    aug = _form_augmented_matrix(A, b)
    aug = _forward_elimination(aug, n, pivot=pivot)
    aug = _backward_substitution(aug, n)
    x = aug[:, n:]
    return x.flatten() if out_1d else x
