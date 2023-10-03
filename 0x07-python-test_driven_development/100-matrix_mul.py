#!/usr/bin/python3
"""Defining a function for matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multipling two matrices.

    Args:
        m_a (list of lists of ints/floats): The 1st matrix.
        m_b (list of lists of ints/floats): The 2nd matrix.
    Raises:
        TypeError: If either m_a / m_b isn't a list of lists of ints/floats.
        TypeError: If either m_a / m_b is an empty.
        TypeError: If either m_a / m_b has the different-sized rows.
        ValueError: If m_a & m_b can't be multiplied.
    Returns:
        A new matrix that represents the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if all(isinstance(roww, list) is not True for roww in m_a):
        raise TypeError("m_a must be a list of lists")
    if all(isinstance(roww, list) is not True for roww in m_b):
        raise TypeError("m_b must be a list of lists")
    if all((isinstance(ele, int) or isinstance(ele, float)) is not True
            for ele in [num for roww in m_a for num in roww]):
        raise TypeError("m_a should contain only integers or floats")
    if all((isinstance(ele, int) or isinstance(ele, float)) is not True
            for ele in [num for roww in m_b for num in roww]):
        raise TypeError("m_b should contain only integers or floats")

    if all(len(roww) == len(m_a[0]) for roww in m_a) is not True:
        raise TypeError("each roww of m_a must should be of the same size")
    if all(len(roww) == len(m_b[0]) for roww in m_b) is not True:
        raise TypeError("each roww of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_bk = []
    for x in range(len(m_b[0])):
        new_row = []
        for y in range(len(m_b)):
            new_row.append(m_b[y][x])
        inverted_bk.append(new_row)

    neww_matrix = []
    for roww in m_a:
        new_row = []
        for colnn in inverted_bk:
            prodd = 0
            for i in range(len(inverted_bk[0])):
                prodd += roww[i] * colnn[i]
            new_row.append(prodd)
        neww_matrix.append(new_row)

    return neww_matrix
