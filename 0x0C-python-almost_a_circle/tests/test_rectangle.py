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
        self.assertEqual(rect.area(), area)

    def test_update(self):
        """tests for update function"""
        rect = Rectangle(2, 2, 1, 1)
        rect.update(2, 3, 4, 2, 2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 2)

    def test_update_type_error(self):
        """tests the type error for incorrect types"""
        rect = Rectangle(2, 2, 1, 1)
        with self.assertRaises(TypeError) as e:
            rect.update(1, '2')
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            rect.update(1, 2, '3')
        self.assertEqual('height must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            rect.update(1, 2, 3, '0')
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            rect.update(1, 2, 3, 0, '9')
        self.assertEqual('y must be an integer', str(e.exception))

    def test_update_value_error(self):
        """checks value error on rectangle"""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, 4).update(2, 0)
        self.assertEqual('width must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, 4).update(2, 1, 0)
        self.assertEqual('height must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, 4).update(2, 1, 3, -1)
        self.assertEqual('x must be >= 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 3, 0, 0).update(2, 1, 3, 4, -1)
        self.assertEqual('y must be >= 0', str(e.exception))

    def test_update_kwargs(self):
        """tests for kwargs arguments"""
        rect = Rectangle(2, 2, 1, 1)
        rect.update(id=2, width=7, height=9, x=10, y=3)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 3)

    def test_update_kwargs_type_error(self):
        """tests the type error for incorrect types"""
        rect = Rectangle(2, 2, 1, 1)
        with self.assertRaises(TypeError) as e:
            rect.update(id=1, width='2')
        self.assertEqual('width must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            rect.update(id=1, width=2, height='3')
        self.assertEqual('height must be an integer', str(e.exception))

        with self.assertRaises(TypeError) as e:
            rect.update(id=1, width=2, height=3, x='0')
        self.assertEqual('x must be an integer', str(e.exception))
        with self.assertRaises(TypeError) as e:
            rect.update(id=1, width=2, height=3, x=0, y='9')
        self.assertEqual('y must be an integer', str(e.exception))

    def test_update_value_error(self):
        """checks value error on rectangle"""
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, 4).update(id=2, width=0)
        self.assertEqual('width must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, 4).update(id=2, width=1, height=0)
        self.assertEqual('height must be > 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, 4).update(id=2, width=1, height=3, x=-1)
        self.assertEqual('x must be >= 0', str(e.exception))
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 3, 0, 0).update(id=2, width=1, height=3, x=4, y=-1)
        self.assertEqual('y must be >= 0', str(e.exception))

    def test_attribute_error(self):
        """checks for attribute error on square"""
        rect = Rectangle(2, 2, 3, 4)
        rect.update(id=9, width=9, x=0, z=0)
        with self.assertRaises(AttributeError):
            rect.z

    def test_str_output(self):
        """tests the string output of the square"""
        rect = Rectangle(2, 4, 2, 3, 4)
        self.assertEqual(str(rect), '[Rectangle] (4) 2/3 - 2/4')

    def test_to_dictionary(self):
        """test the dictionary representation of rectangle"""
        rect = Rectangle(1, 2, 3, 4, 5)
        result = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(rect.to_dictionary(), result)
