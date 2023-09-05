#!/usr/bin/python3
def fizzbuzz():
    for numb in range(1,101):
        if numb % 5 == 0 and numb % 3 == 0:
            print("FizzBuzz",end="")
        elif (numb % 5 == 0):
            print("Buzz",end="")
        elif (numb % 3 == 0):
            print("Fizz",end="")
        else:
            print("{}".format(numb),end="")
