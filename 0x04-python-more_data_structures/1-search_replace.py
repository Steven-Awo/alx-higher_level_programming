#!/usr/bin/python3
def search_replace(my_list, search, replace):
    The_new_list = list(map(lambda z: replace if z == search else z, my_list))
    return (The_new_list)
