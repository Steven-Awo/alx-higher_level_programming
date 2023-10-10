#!/usr/bin/python3
"""Defining a class called Student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing the new Student.

        Args:
            first_name (str): The student's firstname.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Geting a dictionary's representation of the student."""
        return self.__dict__
