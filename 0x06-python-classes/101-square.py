#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """Representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Setting/Getting the square's current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Setting/Getting the square's current position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(isinstance(numb, int) for numb in value) or
                not all(numb >= 0 for numb in value) or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returning the square's current area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Printing out a square made with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")

    def __str__(self):
        """Defining the print() representing a Square."""
        if self.__size != 0:
            [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            if x != self.__size - 1:
                print("")
        return ("")
