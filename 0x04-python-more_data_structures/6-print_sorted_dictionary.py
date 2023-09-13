#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_in_order = list(a_dictionary.keys())
    list_in_order.sort()
    for x in list_in_order:
        print("{}: {}".format(x, a_dictionary.get(x)))
