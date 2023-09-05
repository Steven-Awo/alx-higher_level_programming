#!/usr/bin/python3
for numb in range(0, 100):
    if numb == 99:
        print("{}".format(numb))
    else:
        print("{:02}".format(numb), end=", ")
