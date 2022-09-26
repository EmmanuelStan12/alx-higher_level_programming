#!/usr/bin/python3
"""This module contains a class MyInt that inherits
from int"""


class MyInt(int):
    """This class inherits from int class"""

    def __eq__(self, other):
        """equality operator for int"""
        return super().__ne__(other)

    def __ne__(self, other):
        """not equal operator for int"""
        return super().__eq__(other)
