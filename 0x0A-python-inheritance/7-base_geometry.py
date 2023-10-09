#!/usr/bin/python3
"""Defining the base geometry of class BaseGeometry."""


class BaseGeometry:
    """Reprsenting the base geometry."""

    def area(self):
        """Not yet being implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating the parameter as an int.

        Args:
            name (str): The name belonging to the parameter.
            value (int): The parameter to be validated.
        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value is < or = 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
