#!/usr/bin/python3
"""Defining a class called Student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): The student's firstname.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Getting a dictionary's representation of the class Student.

        If the attrs is actually a list of strings, then represents only the attributes
        thats included in the list.

        Args:
            attrs (list): (Optional) The representation of the attributes.
        """
        if (type(attrs) == list and
                all(type(elemt) == str for elemt in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
