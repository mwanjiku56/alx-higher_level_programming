#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        x = ord(str[c])
        if (x >= 97 and x <= 122):
            x -= 32
        print("{}".format(chr(x)), end="")
    print()
