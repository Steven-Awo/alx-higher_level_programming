#!/usr/bin/python3
"""Defining a square-printing function."""


def print_square(size):
    """Printing a square out using the # character.

    Args:
        size (int): The height or the width of the square.
    Raises:
        TypeError: If size isn't an integer.
        ValueError: If size is < 0
    """
    if isinstance(size, int) is not True:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
