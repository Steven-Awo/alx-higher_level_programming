#!/usr/bin/python3
"""To define a class Square."""


class Square:
    """To represent the class square."""

    def __init__(self, size=0, position=(0, 0)):
        """To initialize the new square.

        Args:
            size (int): The size of new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """To Set or get the current positn of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(numb, int) for numb in value) or
                not all(numb >= 0 for numb in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """To return the square's current area."""
        return (self.__size * self.__size)

    def my_print(self):
        """To print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")

