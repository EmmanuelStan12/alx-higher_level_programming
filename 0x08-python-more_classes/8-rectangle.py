#!/usr/bin/python3
"""
This module describes a Rectangle class and it's functionality
"""


class Rectangle:
    """
    Rectangle class Implementation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """computes the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """computes the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """prints the rectangle with '#' sign"""
        rect = ''
        for i in range(self.height):
            rect += self.width * str(self.print_symbol)
            if i != self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """gives an object representation of the given instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """clean up before an instance is deleted"""
        print("Bye rectangle...")
        if self.__class__.number_of_instances != 0:
            self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks for the biggest rectangle amongst both"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
