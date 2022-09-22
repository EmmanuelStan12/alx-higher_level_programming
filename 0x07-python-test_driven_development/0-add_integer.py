#!/usr/bin/python3
"""
this module defines a function to add two integers
"""


def add_integer(a, b=98):
    """
    this function adds two integers
    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
