#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Setting/Getting the square's current position."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returning the squaares current area."""
        return (self.__size * self.__size)

    def __ne__(self, other):
        """Defining the != comparing to a Square."""
        return self.area() != other.area()

    def __eq__(self, other):
        """Defining the == comparing to a Square."""
        return self.area() == other.area()

    def __gt__(self, other):
        """Defining the > comparing to a Square."""
        return self.area() > other.area()

    def __lt__(self, other):
        """Defining the < comparing to a Square."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Defining the >= comparing to a Square."""
        return self.area() >= other.area()
    def __le__(self, other):
        """Defining the <= comparing to a Square."""
        return self.area() <= other.area()
