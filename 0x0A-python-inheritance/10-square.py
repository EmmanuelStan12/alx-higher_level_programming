#!/usr/bin/python3
"""This module contains a Square class that
inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__size * self.__size
