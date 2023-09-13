#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_diry = a_dictionary.copy()
    list_of_keys = list(new_diry.keys())
    for x in list_of_keys:
        new_diry[x] *= 2
    return (new_diry)
