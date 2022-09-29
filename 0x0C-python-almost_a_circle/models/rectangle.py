#!/usr/bin/python3
"""this module has a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """this class defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width property getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width property"""
        self.__width = value

    @property
    def height(self):
        """declaring height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height property"""
        self.__height = value

    @property
    def x(self):
        """declaring x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x property"""
        self.__x = value

    @property
    def y(self):
        """declaring y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y property"""
        self.__y = value
