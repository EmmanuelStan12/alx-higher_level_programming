#!/usr/bin/python3
"""This module contains a class Base Geometry"""


class BaseGeometry:
    """Base Geometry class for geometry"""
    
    def area(self):
        """checks area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
