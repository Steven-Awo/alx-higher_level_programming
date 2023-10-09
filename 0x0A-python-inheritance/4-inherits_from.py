#!/usr/bin/python3
"""Defining the class function inherited class-checking."""


def inherits_from(obj, a_class):
    """Checking if an object is truly an inherited instance of any class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be matched by the type of obj to.
    Returns:
        If the obj is truly an inherited instance of the class a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return True
    return False
