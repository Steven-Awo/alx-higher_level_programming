#!/usr/bin/python3
"""Defining new a Rectangle class."""


class Rectangle:
    """Representation the new rectangle."""

    def __init__(self, width=0, height=0):
        """Initializating a new Rectangle.

        Args:
            height (int): The height of the new rectangle.
            width (int): The width of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting/setting the width of the new rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value == 0 or value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting/setting the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value == 0 or value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
