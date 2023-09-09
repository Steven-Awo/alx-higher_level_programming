#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for roww in matrix:
        for colm in roww:
            print("{:d}".format(colm), end=" " if colm != roww[-1] else "")
        print()
