#!/usr/bin/python3
""" Program that returns the number of lines """


def number_of_lines(filename=""):
    """ function that returns the number of lines of a text file """
    count = 0
    with open(filename) as j:
        for line in j:
            count += 1
    return (count)
    