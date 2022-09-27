#!/usr/bin/python3
"""This module contains a class that defines a student"""


class Student:
    """This class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student variable"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the class"""
        return self.__dict__
