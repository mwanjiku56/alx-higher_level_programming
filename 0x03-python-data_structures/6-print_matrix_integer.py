#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for a in range(len(matrix)):
        for x in range(len(matrix[a])):
                print("{:d}".format(matrix[a][x]), end="")
                if x != (len(matrix[a]) - 1):
                    print(" ", end="")

        print("")
