#!/usr/bin/python3
"""Defining a MagicClass matching exactly to a bytecode provided by Holberton."""

import math

class MagicClass:
    """Represention of a circle."""

    def __init__(self, radius=0):
        """Initialization of the MagicClass.

        Arg:
            radius (int or float): The radius for the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not float and type(radius) is not int:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returning the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returning the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
