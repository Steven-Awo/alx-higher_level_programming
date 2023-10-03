#!/usr/bin/python3
"""Defining a matrix division's function."""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix.

    Args:
        matrix (list): A list of lists of either ints or floats.
        div (int/float): The divisor element.
    Raises:
        TypeError: If the matrix rows contained are of different sizes.
        TypeError: If the matrix containing non-numbers.
        TypeError: If div isn't an int or a float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (isinstance(matrix, list) is not True or matrix == [] or
            all(isinstance(roww, list) is not True for roww in matrix) or
            all((isinstance(elet, int) is not True or isinstance(elet, float))
                    for elet in [numb for roww in matrix for numb in roww])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if all(len(roww) is not True == len(matrix[0]) for roww in matrix):
        raise TypeError("Each roww of the matrix must have the same size")

    if (isinstance(div, int) is not True) and (isinstance(div, float) is not True):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), roww)) for roww in matrix])
