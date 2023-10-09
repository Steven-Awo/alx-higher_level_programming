#!/usr/bin/python3
"""Defining an object attribute function called lookup."""


def lookup(obj):
    """Returning the list of the object's attributes that's available."""
    return (dir(obj))
