#!/usr/bin/python3
"""Defining the function called string-to-JSON."""
import json


def to_json_string(my_obj):
    """Returning the JSON file representation of the string object."""
    return json.dumps(my_obj)
