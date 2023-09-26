#!/usr/bin/python3
"""to define a class Square."""


class Square:
    """to represent a square."""

    def __init__(self, size="0"):
        """to initialize the new Square class.

        Args:
            size (int): The size of  new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """To Return the current area to the square."""
        return (self.__size * self.__size)
