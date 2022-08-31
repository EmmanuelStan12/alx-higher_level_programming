#!/usr/bin/python3
def uniq_add(my_list=[]):
    set = {i for i in my_list}
    sum = 0
    for i in set:
        sum = sum + i
    return sum
