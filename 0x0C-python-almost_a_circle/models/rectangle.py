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
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(self.x * ' ' + self.width * '#')

    def __str__(self):
        """returns the string representation of the instance"""
        result = "[Rectangle] ({}) {}/{} - {}/{}"
        f = result.format(self.id, self.x, self.y, self.width, self.height)
        return f

    def update(self, *args, **kwargs):
        """updates the varibles of the instance"""
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
                    self.width = args[i]
                case 2:
                    self.height = args[i]
                case 3:
                    self.x = args[i]
                case 4:
                    self.y = args[i]

    def __update_kwargs(self, kwargs):
        """updates the variables of the instance with dictionary"""
        keys = ['width', 'height', 'x', 'y', 'id']
        for i, (key, value) in enumerate(kwargs.items()):
            if key in keys:
                setattr(self, key, value)

    def to_dictionary(self):
        """transforms the rectangle instance to a dictionary"""
        dict = {}
        keys = ['id', 'width', 'height', 'x', 'y']
        for i, (k, v) in enumerate(self.__dict__.items()):
            key = k.replace('_Rectangle__', '')
            if key in keys:
                dict[key] = v
        return dict
