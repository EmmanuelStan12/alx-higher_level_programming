#!/usr/bin/python3
def uppercase(str):
    i = 0
    if len(str) == 0:
        print("{}".format(str))
    for char in str:
        value = ord(char)
        if value >= 97 and value <= 122:
            char = chr(value - 32)
        if i == len(str) - 1:
            delim = '\n'
        else:
            delim = ''
        print("{}".format(char), end=delim)
        i = i + 1
