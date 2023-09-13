#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    numb = 0
    for x in unique_list:
        numb = numb + x
    return (numb)
