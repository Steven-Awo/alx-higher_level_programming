#!/usr/bin/python3
"""Defining a class and also inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checking if an object that's in an instance or is inherited by
    instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be matched by the type of obj to.
    Returns:
        If the obj is truly an instance/inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class) is True:
        return True
    return False
