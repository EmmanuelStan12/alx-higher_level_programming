#!/usr/bin/python3

"""
This module describes a Square class and it's functionality
"""


class Square:
    """
    Note:
        Square class
    Args:
        size (int): the size of the string.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        finds the area of the square
        """
        return self.__size * self.__size
