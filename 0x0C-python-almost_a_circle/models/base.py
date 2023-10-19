#!/usr/bin/python3

class Base:
    """Defining a class called base model."""

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
