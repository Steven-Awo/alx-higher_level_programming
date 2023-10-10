#!/usr/bin/python3
"""Defining the function JSON-to-object."""
import json


def from_json_string(my_str):
    """Returning the Python's object that represent a JSON string."""
    return json.loads(my_str)
