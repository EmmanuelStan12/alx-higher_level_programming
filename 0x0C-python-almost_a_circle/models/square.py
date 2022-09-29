#!/usr/bin/python3
"""this module creates a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for property size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the instance"""
        f = "[Square] ({}) {}/{} - {}"
        return f.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates the instances variables"""
        if len(args) != 0:
            self.__update_args(args)
        else:
            self.__update_kwargs(kwargs)

    def __update_args(self, args):
        """updates the arguments of the instance"""
        for i in range(len(args)):
            match i:
                case 0:
                    self.id = args[i]
                case 1:
                    self.size = args[i]
                case 2:
                    self.x = args[i]
                case 3:
                    self.y = args[i]

    def __update_kwargs(self, kwargs):
        """updates the variables of the instance with dictionary"""
        keys = ['size', 'x', 'y', 'id']
        for i, (key, value) in enumerate(kwargs.items()):
            if key in keys:
                setattr(self, key, value)
