#!/usr/bin/python3
def fizzbuzz():
    for numb in range(1,101):
        if numb % 5 == 0 and numb % 3 == 0:
            print("FizzBuzz")
        elif (numb % 5 == 0):
            print("Buzz")
        elif (numb % 3 == 0):
            print("Fizz")
        else:
            print("{}".format(numb))
