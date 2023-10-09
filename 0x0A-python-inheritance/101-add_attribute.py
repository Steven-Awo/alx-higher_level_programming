#!/usr/bin/python3
"""Defining the function that adds the attributes to the objects."""


def add_attribute(obj, att, value):
    """Adding the new attribute to an object if its possible.

    Args:
        obj (any): The object that an attribute is to be added to.
        att (str): The name that an attribute is to be added  to obj.
        value (any): The value ofthe att.
    Raises:
        TypeError: If adding the attribute isn't possible.
    """
    if hasattr(obj, "__dict__") is not True:
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
