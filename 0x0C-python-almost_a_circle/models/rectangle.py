#!/usr/bin/python3
"""this module has a rectangle class"""
from models.base import Base

class Rectangle(Base):
    """this class defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id) 
        self.__run_checker(width, height, x, y)
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
        self.__checker("width", value)
        self.__width = value

    @property
    def height(self):
        """declaring height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height property"""
        self.__checker("height", value)
        self.__height = value

    @property
    def x(self):
        """declaring x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x property"""
        self.__checker("x", value)
        self.__x = value

    @property
    def y(self):
        """declaring y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y property"""
        self.__checker("y", value)
        self.__y = value

    def __run_checker(self, width, height, x, y):
        """runs checker for all attributes"""
        self.__checker("width", width)
        self.__checker("height", height)
        self.__checker("x", x)
        self.__checker("y", y)

    def __checker(self, name, value):
        """checks for valid values of attributes"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name == "height" or name == "width":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """checks for the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the instance as a string of '#' characters"""
        for i in range(self.height):
            print(self.width * '#')
