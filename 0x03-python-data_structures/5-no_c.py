#!/usr/bin/python3
def no_c(my_string):
    for a in range(len(my_string) - 2):
        if (my_string[a] == 'c' or my_string[a] == 'C'):
            my_string = my_string[:a] + "" + my_string[a+1:]
    return (my_string)
    