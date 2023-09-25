#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    retrn = 0
    for y in range(0, x):
        try:
            print("{:d}".format(my_list[y]), end="")
            retrn += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (retrn)
