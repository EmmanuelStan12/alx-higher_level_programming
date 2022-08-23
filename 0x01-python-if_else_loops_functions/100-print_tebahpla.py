#!/usr/bin/python3
i = 1
for char in "zyxwvutsrqponmlkjihgfedcba":
    value = ord(char)
    if i % 2 == 0:
        print("{}".format(chr(value - 32)), end='')
    else:
        print("{}".format(char), end='')
    i = i + 1
