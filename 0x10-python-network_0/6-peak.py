#!/usr/bin/python3
"""Finding a peak thats in a list of an unsorted ints"""


def find_peak(list_of_ints):
    """Finding the peak in the list_of_ints"""

    if list_of_ints is None or list_of_ints == []:
        return None
    lowr = 0
    higr = len(list_of_ints)
    midle = ((higr - lowr) // 2) + lowr
    midle = int(midle)
    if higr == 1:
        return list_of_ints[0]
    if higr == 2:
        return max(list_of_ints)
    if list_of_ints[midle] >= list_of_ints[midle - 1] and\
            list_of_ints[midle] >= list_of_ints[midle + 1]:
        return list_of_ints[midle]
    if midle > 0 and list_of_ints[midle] < list_of_ints[midle + 1]:
        return find_peak(list_of_ints[midle:])
    if midle > 0 and list_of_ints[midle] < list_of_ints[midle - 1]:
        return find_peak(list_of_ints[:midle])
