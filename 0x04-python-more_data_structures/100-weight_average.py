#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    total = 0
    for score, weight in my_list:
        sum = sum + score * weight
        total = total + weight
    return sum / total
