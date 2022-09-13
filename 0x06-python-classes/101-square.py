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
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position) is tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
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
        y = self.__position[1]
        x = self.__position[0]
        for i in range(y):
            print()
        for i in range(self.__size):
            for k in range(x):
                print(' ', end='')
            for j in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        """returns the position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """value: new value of position"""
        if type(value) is tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """returns the square with '#' characters"""
        s = ""
        if self.__size == 0:
            s += '\n'
            return s
        y = self.__position[1]
        x = self.__position[0]
        for i in range(y):
            s += '\n'
        for i in range(self.__size):
            for k in range(x):
                s += ' '
            for j in range(self.__size):
                s += '#'
            if i < self.__size - 1:
                s += '\n'
        return s
