#!/usr/bin/python3
def max_integer(my_list=[]):
    max = float('-inf')
    for num in my_list:
        if num > max:
            max = num
    return max
