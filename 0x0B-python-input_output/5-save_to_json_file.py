#!/usr/bin/python3
"""Defining the function JSON file-writing."""
import json


def save_to_json_file(my_obj, filename):
    """Writing from an object to the text file thats using the JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
