#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        s = ""
        for b in a:
            print("{:s}{:d}".format(s, b, end='')
            s = " "
        print()
