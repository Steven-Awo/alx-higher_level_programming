#!/usr/bin/python3
def uppercase(str):
    for chrr in str:
        if ord(chrr) >= 97 and ord(chrr) <= 122:
            chrr = chr(ord(chrr) - 32)
        print("{}".format(chrr), end="")
    print("")
