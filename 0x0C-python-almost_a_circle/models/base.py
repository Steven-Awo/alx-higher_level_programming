#!/usr/bin/python3

"""Defining a class called base model."""

class Base:
    """A representation of the base of our OOP hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the neww Base.

        Args:
            id (int): The neww base identity.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
