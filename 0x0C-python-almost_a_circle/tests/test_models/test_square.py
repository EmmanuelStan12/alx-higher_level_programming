#!/usr/bin/python3
"""this module tests the rectangle class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """this class tests the rectangle class"""

    def test_rect_correct_init(self):
        """tests the initialization of the class"""
        sqr = Square(2, 1, 1)
        self.assertEqual(sqr.size, 2)
        self.assertEqual(sqr.x, 1)
        self.assertEqual(sqr.y, 1)

    def test_type_error(self):
        """tests the type error for incorrect types"""
        with self.assertRaises(TypeError) as we:
            Square('2', 0, 0)
        self.assertEqual('width must be an integer', str(we.exception))
        with self.assertRaises(TypeError) as hve:
            Square(1, '0', 0)
        self.assertEqual('x must be an integer', str(hve.exception))
        with self.assertRaises(TypeError) as wve:
            Square(2, 0, '0')
        self.assertEqual('y must be an integer', str(wve.exception))

    def test_value_error(self):
        """checks value error on rectangle"""
        with self.assertRaises(ValueError) as e:
            Square(0, 0, 0)
        self.assertEqual('width must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Square(2, -1, 0)
        self.assertEqual('x must be >= 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Square(3, 0, -2)
        self.assertEqual('y must be >= 0', str(e.exception))

    def test_area(self):
        """checks for the area of the rectangle"""
        area = 9
        sqr = Square(3, 1, 1)
        self.assertEqual(sqr.area(), area)

    def test_update(self):
        """tests for update function"""
        sqr = Square(2, 1, 1)
        sqr.update(3, 4, 2, 2)
        self.assertEqual(sqr.id, 3)
        self.assertEqual(sqr.size, 4)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 2)

    def test_update_type_error(self):
        """tests the type error for incorrect types"""
        s = Square(2, 1, 1)
        with self.assertRaises(TypeError) as e:
            s.update(1, '2')
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            s.update(1, 2, '3')
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            s.update(1, 2, 0, '9')
        self.assertEqual('y must be an integer', str(e.exception))

    def test_update_value_error(self):
        """checks value error on rectangle"""
        with self.assertRaises(ValueError) as e:
            Square(1, 3, 4).update(2, 0)
        self.assertEqual('width must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Square(1, 3, 4).update(2, 1, -1)
        self.assertEqual('x must be >= 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Square(1, 3, 0, 0).update(2, 1, 3, -1)
        self.assertEqual('y must be >= 0', str(e.exception))

    def test_update_kwargs(self):
        """tests for kwargs arguments"""
        sqr = Square(2, 1, 1)
        sqr.update(id=2, size=7, x=10, y=3)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 7)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 3)

    def test_update_kwargs_type_error(self):
        """tests the type error for incorrect types"""
        s = Square(2, 1, 1)
        with self.assertRaises(TypeError) as e:
            s.update(id=1, size='2')
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            s.update(id=1, size=2, x='0')
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            s.update(id=1, size=2, x=0, y='9')
        self.assertEqual('y must be an integer', str(e.exception))

    def test_update_value_error(self):
        """checks value error on rectangle"""
        with self.assertRaises(ValueError) as e:
            Square(2, 3, 4).update(id=2, size=0)
        self.assertEqual('width must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Square(2, 3, 4).update(id=2, size=1, x=-1)
        self.assertEqual('x must be >= 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Square(3, 0, 0).update(id=2, size=3, x=4, y=-1)
        self.assertEqual('y must be >= 0', str(e.exception))

    def test_attribute_error(self):
        """checks for attribute error on square"""
        sqr = Square(2, 3, 4)
        sqr.update(id=9, size=9, x=0, z=0)
        with self.assertRaises(AttributeError):
            sqr.z

    def test_str_output(self):
        """tests the string output of the square"""
        sqr = Square(4, 2, 3, 4)
        self.assertEqual(str(sqr), '[Square] (4) 2/3 - 4')

    def test_to_dictionary(self):
        """test the dictionary representation of a square"""
        sqr = Square(2, 3, 4, 5)
        result = {'x': 3, 'y': 4, 'id': 5, 'size': 2}
        self.assertEqual(sqr.to_dictionary(), result)
