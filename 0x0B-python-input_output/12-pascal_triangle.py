#!/usr/bin/python3
"""Defining the function class called Pascal's Triangle."""


def pascal_triangle(n):
    """Representation of the Pascal's Triangle of the size n.

    Returning a list of lists of the integers that represents the triangle.
    """
    if n <= 0:
        return []

    trigles = [[1]]
    while len(trigles) != n:
        tri_angle = trigles[-1]
        tempr = [1]
        for x in range(len(tri_angle) - 1):
            tempr.append(tri_angle[x] + tri_angle[x + 1])
        tempr.append(1)
        trigles.append(tempr)
    return trigles
