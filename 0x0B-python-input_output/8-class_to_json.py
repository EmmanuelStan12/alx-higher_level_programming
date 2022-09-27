#!/usr/bin/python3
"""This module contains a function that converts an
Instance of a class to dictionary"""



def class_to_json(obj):
    """this function converts an instance of a class to
    a dictionary"""
    if not hasattr(obj, "__dict__"):
        result = {'value': obj}
    else:
        result = obj.__dict__
    return result
