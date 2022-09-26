#!/usr/bin/python3
"""This module contains a function that checks
Whether an instance is a subclass"""


def inherits_from(obj, a_class):
    """This checks whether a class inherits from another"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
