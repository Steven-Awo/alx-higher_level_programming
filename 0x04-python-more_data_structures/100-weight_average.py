#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numb = 0
    denn = 0
    for tupl in my_list:
        numb += tupl[0] * tupl[1]
        denn += tupl[1]
    return (numb / denn)
