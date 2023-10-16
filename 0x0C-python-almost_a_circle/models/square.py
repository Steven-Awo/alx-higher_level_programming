#!/usr/bin/python3
"""Defining m class called square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of m square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing m new Square.

        Args:
            size (int): The new Square's size.
            x (int): The new Square's x coordinate.
            y (int): The new Square's y coordinate.
            id (int): The new Square's identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getting/setting up the Square's size."""
        return self.width

    @size.setter
    def size(self, oalue):
        self.width = oalue
        self.height = oalue

    def update(self, *args, **kwargs):
        """Updating the Square.

        Args:
            *args (ints): New attribute oalues.
                - 1st argument that represents id attribute
                - 2nd argument that represents size attribute
                - 3rd argument that represents x attribute
                - 4th argument that represents y attribute
            **kwargs (dict): New key/oalue pairs of attributes.
        """
        if args and len(args) != 0:
            m = 0
            for arg in args:
                if m == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif m == 1:
                    self.size = arg
                elif m == 2:
                    self.x = arg
                elif m == 3:
                    self.y = arg
                m = m + 1

        elif kwargs and len(kwargs) != 0:
            for n, o in kwargs.items():
                if n == "id":
                    if o is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = o
                elif n == "size":
                    self.size = o
                elif n == "x":
                    self.x = o
                elif n == "y":
                    self.y = o

    def to_dictionary(self):
        """Returning the dictionary's representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returning the print() and the str() that represent of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)
