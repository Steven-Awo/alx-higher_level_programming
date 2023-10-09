#!/usr/bin/python3
"""Defining a fuction called class-checking."""


def is_same_class(obj, a_class):
    """Checking if there's an object thats is exactly an
    instance of the given class.

    Args:
        obj (any): The object used to check.
        a_class (type): The class to be match by the type of obj to.
    Returns:
        If obj is truly an instance of a_class - True.
        Otherwise - print False.
    """
    if type(obj) == a_class:
        return True
    return False
