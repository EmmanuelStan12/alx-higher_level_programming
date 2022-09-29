#!/usr/bin/python3
"""this module creates a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the instance"""
        f = "[Square] ({}) {}/{} - {}"
        return f.format(self.id, self.x, self.y, self.width)
