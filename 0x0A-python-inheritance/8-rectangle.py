#!/usr/bin/python3
"""Defining a class Rectangle that can inherit from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rectangle  that uses BaseGeometry."""

    def __init__(self, width, height):
        """Intializng a new Rectangle.

        Args:
            width (int): The new width of the newly created Rectangle.
            height (int): The new height of the newly created Rectangle.
        """
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
