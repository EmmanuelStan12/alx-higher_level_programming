#!/usr/bin/python3
"""This module contains a class that defines a student"""


class Student:
    """This class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student variable"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the class"""
        if type(attrs) != list:
            return self.__dict__
        new_dict = {}
        for key in attrs:
            if (key in self.__dict__) and (key not in new_dict):
                new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
        """Returns an instance of a class from json object"""
        for key in json:
            if key in self.__dict__:
                setattr(self, key, json[key])
