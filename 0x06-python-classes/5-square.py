#!/usr/bin/python3

"""This module describes a Square class and it's functionality
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

    @property
    def size(self):
        """size: the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets a size based on constraints"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints the square with '#' characters"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
