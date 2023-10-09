#!/usr/bin/python3
"""Defining a Rectangle's subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representing a square."""

    def __init__(self, size):
        """Initializing the new square.

        Args:
            size (int): The size of the newly created square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
