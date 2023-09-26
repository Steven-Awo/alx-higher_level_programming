#!/usr/bin/python3
"""To define a class Square."""


class Square:
    """To represent the class square."""

    def __init__(self, size=0):
        """To initialize the new square.

        Args:
            size (int): The size of new square.
        """
        self.size = size

    @property
    def size(self):
        """To Set or get the current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """To return the square's current area."""

        return (self.__size * self.__size)
    def my_print(self):
        """To print out the square with the # char."""

        for x in range(0, self.__size):
            [print("#", end="")
                    for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
