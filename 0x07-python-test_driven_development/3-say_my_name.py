#!/usr/bin/python3
"""Defining a fuction called name-printing."""


def say_my_name(first_name, last_name=""):
    """Printing a name.

    Args:
        first_name (str): The 1st name to be printed.
        last_name (str): The last name to be printed.
    Raises:
        TypeError: If either of the names are not strings.
    """
    if isinstance(first_name, str) is not True:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
