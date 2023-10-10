#!/usr/bin/python3
"""Defining fuction of a text file-reading."""


def read_file(filename=""):
    """Printing the UTF8 text file contents to the stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
