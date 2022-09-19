#!/usr/bin/python3
"""
this module contains a function that prints a square
"""


def print_square(size):
    if type(size) == float and size < 0:
        raise TypeError("size must be >= 0")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size * '#')
        
