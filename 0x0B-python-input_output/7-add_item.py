#!/usr/bin/python3
"""Adding all the arguments to the Python list and saving them to the file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        itms = load_from_json_file("add_item.json")
    except FileNotFoundError:
        itms = []
    itms.extend(sys.argv[1:])
    save_to_json_file(itms, "add_item.json")
