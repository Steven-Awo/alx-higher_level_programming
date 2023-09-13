#!/usr/bin/python3
def number_keys(a_dictionary):
    numbr = 0
    d_list_keys = list(a_dictionary.keys())
    for x in d_list_keys:
        numbr = numbr + 1
    return (numbr)
