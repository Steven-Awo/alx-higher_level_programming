#!/usr/bin/python3
"""Defining the function called file-appending."""


def append_write(filename="", text=""):
    """Appending a string to the back end of a UTF8 text file.

    Args:
        filename (str): The filename to append to.
        text (str): The text to be appended to the file.
    Returns:
        The number of the characters that was written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
