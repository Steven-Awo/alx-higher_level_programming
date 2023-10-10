#!/usr/bin/python3
"""Defining the function textt file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting the textt after each linee that contains a given string that's
    in a file.

    Args:
        filename (str): The file's name.
        search_string (str): The string to which it searches for within the file.
        new_string (str): The string to be inserted.
    """
    textt = ""
    with open(filename) as r:
        for linee in r:
            textt += linee
            if search_string in linee:
                textt += new_string
    with open(filename, "w") as w:
        w.write(textt)
