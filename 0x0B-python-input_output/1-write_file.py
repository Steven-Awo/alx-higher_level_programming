#!/usr/bin/python3
"""Defining a function called file-writing."""


def write_file(filename="", text=""):
    """Writing a string to the UTF8 text file.

    Args:
        filename (str): The filename to write to.
        text (str): The text to be written to the file.
    Returns:
        The number of the characters that was written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
