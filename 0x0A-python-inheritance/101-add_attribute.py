#!/usr/bin/python3
"""This module contains a function that
checks if a new attribute can be added
"""


def add_attribute(instance, name, value):
    """Adds a variable to an instance"""
    if not hasattr(instance, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(instance, name, value)
