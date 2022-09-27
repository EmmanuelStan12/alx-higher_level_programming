#!/usr/bin/python3
"""This module contains a function that returns a list of
integers representing pascal's triangle"""


def pascal_triangle(n):
    """this function returns a list of integers"""
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
            continue
        elif i == 1:
            result.append([1, 1])
            continue
        prev_list = result[i - 1]
        row = [1]
        for j in range(len(prev_list)):
            if (j + 1) != len(prev_list):
                row.append(prev_list[j] + prev_list[j + 1])
        row.append(1)
        result.append(row)
    return result
