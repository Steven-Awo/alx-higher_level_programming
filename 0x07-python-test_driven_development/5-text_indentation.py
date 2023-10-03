#!/usr/bin/python3
# 5-text_indentation.py
"""Defining a text-indentation function."""


def text_indentation(text):
    """Printing each text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If text isn't a string.
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
