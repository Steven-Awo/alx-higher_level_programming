#!/usr/bin/python3
"""Defining a rectangle class Rectangle inherits from the BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializing a new Rectangle.

        Args:
            width (int): The new width of the newly created Rectangle.
            height (int): The new height of the newly created Rectangle.
        """
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """Returning the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Returning the str() and the print() representing a rectangle."""
        strng = "[" + str(self.__class__.__name__) + "] "
        strng += str(self.__width) + "/" + str(self.__height)
        return strng
