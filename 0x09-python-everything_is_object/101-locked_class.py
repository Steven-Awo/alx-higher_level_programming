#!/usr/bin/python3
"""Defining a locked class."""


class LockedClass:
    """
    Preventing the user from starting new LockedClass attributes
    for anything but the attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
