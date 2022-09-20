#!/usr/bin/python3
"""
This module has a class that prevents the user from creating certain attributes
"""


class LockedClass():
    """
    Locked class Implementation
    """
    def __setattr__(self, key, value):
        message = "'LockedClass' object has no attribute '{}'"
        if key != 'first_name':
            raise AttributeError(message.format(key))
        else:
            object.__setattr__(self, key, value)
