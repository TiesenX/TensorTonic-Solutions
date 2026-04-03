import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A_np = np.array(A)
    rows, cols = A_np.shape
    A_T = np.zeros((cols, rows))
    for r in range(rows):
        for c in range(cols):
            A_T[c, r] = A_np[r, c]
    return A_T
