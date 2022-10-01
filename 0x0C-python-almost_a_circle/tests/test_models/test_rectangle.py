#!/usr/bin/python3
"""this module tests the rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """this class tests the rectangle class"""
    
    def test_rect_correct_init(self):
        """tests the initialization of the class"""
        rec1 = Rectangle(2, 2, 1, 1)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 2)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec1.y, 1)

    def test_type_error(self):
        """tests the type error for incorrect types"""
        with self.assertRaises(TypeError) as we:
            Rectangle('1', 2, 0, 0)
        self.assertEqual('width must be an integer', str(we.exception))
        with self.assertRaises(TypeError) as he:
            Rectangle(1, '2', 0, 0)
        self.assertEqual('height must be an integer', str(he.exception))
        with self.assertRaises(TypeError) as hve:
            Rectangle(2, 1, '0', 0)
        self.assertEqual('x must be an integer', str(hve.exception))
        with self.assertRaises(TypeError) as wve:
            Rectangle(1, 2, 0, '0')
        self.assertEqual('y must be an integer', str(wve.exception))

    def test_value_error(self):
        """checks value error on rectangle"""
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2, 0, 0)
        self.assertEqual('width must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0, 0, 0)
        self.assertEqual('height must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -1, 0)
        self.assertEqual('x must be >= 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 3, 0, -2)
        self.assertEqual('y must be >= 0', str(e.exception))

    def test_area(self):
        """checks for the area of the rectangle"""
        area = 15
        rect = Rectangle(3, 5, 1, 1)
        assertEqual(rect.area(), area)
