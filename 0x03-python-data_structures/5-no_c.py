#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new_str = ''
    for str in my_string:
        if str != 'c' and str != 'C':
            new_str = new_str + str
    return new_str
