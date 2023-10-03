#!/usr/bin/python3
"""Defining an integer additional function."""


def add_integer(a, b=98):
    """Returning the integer addition of the values a and b.

    Float arguments are actually typecasted to the ints before addition
    is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if (isinstance(a, int) is not True) and (isinstance(a, float) is not True):
        raise TypeError("a must be an integer")
    if (isinstance(b, int) is not True) and (isinstance(b, float) is not True):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
