#!/usr/bin/python3
"""
This module has a class that prevents the user from creating certain attributes
"""


class LockedClass():
    """
    Locked class Implementation
    """
    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(key))
        else:
            object.__setattr__(self, key, value)
