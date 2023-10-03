#!/usr/bin/python3
"""Defining a matrix of multiplication function using the NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returning the multiple of two matrices.

    Args:
        m_a (list of lists of ints/floats): The 1st matrix.
        m_b (list of lists of ints/floats): The 2nd matrix.
    """

    return (np.matmul(m_a, m_b))
