#!/usr/bin/python3
"""Defining the function of Python class-to-JSON."""


def class_to_json(obj):
    """Returning the dictionary that represnts a simple data structure."""
    return obj.__dict__
