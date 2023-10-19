#!/usr/bin/python3
"""Module for the class base model."""

class Base:
    """the Base model.
    Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the neww Base.

        Args:
            id (int): The neww base identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
