#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    countz = len(sys.argv) - 1
    if countz == 0:
        print("0 arguments.")
    elif countz == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(countz))
    for i in range(countz):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
