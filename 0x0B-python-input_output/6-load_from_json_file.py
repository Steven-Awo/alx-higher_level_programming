#!/usr/bin/python3
"""Defining the function JSON file-reading."""
import json


def load_from_json_file(filename):
    """Creating the Python object from the JSON file."""
    with open(filename) as f:
        return json.load(f)
