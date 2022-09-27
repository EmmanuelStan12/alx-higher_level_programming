#!/usr/bin/python3
"""This module contains a class MyInt that inherits
from int
"""


class MyInt(int):
    """This class inherits from directly from the int class"""

    def __eq__(self, other):
        """checks for equality operator for the int class"""
        return super().__ne__(self, other)

    def __ne__(self, other):
        """checks for none equality operator for int class"""
        return super().__eq__(self, other)
