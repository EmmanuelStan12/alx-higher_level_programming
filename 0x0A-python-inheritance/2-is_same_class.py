#!/usr/bin/python3
"""This module contains a function that checks
if a class is an instance of another
"""


def is_same_class(obj, a_class):
    """A function that returns whether both objs are same"""

    return type(obj) == a_class
