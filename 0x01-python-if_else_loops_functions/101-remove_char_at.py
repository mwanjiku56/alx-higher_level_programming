#!/usr/bin/python3
def remove_char_at(str, x):
    if x >= 0:
        newstr = str[:x] + str[x + 1:]
    else:
        newstr = str
    return (newstr)
    