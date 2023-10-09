#!/usr/bin/python3
"""Defining a class called MyInt that inherits info from int."""


class MyInt(int):
    """Inverting the int operators == and the !=."""

    def __eq__(self, value):
        """Overriding == opeartor with  the != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overriding the != operator with the == behavior."""
        return self.real == value
