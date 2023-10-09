#!/usr/bin/python3
"""Defining a new inherited list of class called MyList."""


class MyList(list):
    """Implementing a sorted that prints for the built-in list class."""

    def print_sorted(self):
        """Printing a list thats sorted in an ascending order."""
        print(sorted(self))
