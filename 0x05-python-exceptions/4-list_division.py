#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    the_new_list = []
    for x in range(0, list_length):
        try:
            divd = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            divd = 0
        except TypeError:
            print("wrong type")
            divd = 0
        except IndexError:
            print("out of range")
            divd = 0
        finally:
            the_new_list.append(divd)
    return (the_new_list)
