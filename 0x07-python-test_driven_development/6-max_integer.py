#!/usr/bin/python3
"""Module to be able to find the max integer in a list
"""


def max_integer(list=[]):
    """Functioning to find and also return the max integer in a list of
        integers
        If the list is an empty list, the function should returns None
    """
    if len(list) == 0:
        return None
    soln = list[0]
    x = 1
    while x < len(list):
        if list[x] > soln:
            soln = list[x]
        x += 1
    return soln
