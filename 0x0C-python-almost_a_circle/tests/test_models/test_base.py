#!/usr/bin/python3
"""this module tests the base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """this class tests the base class"""
    
    def test_base_default_id(self):
        """tests the id assigned to the class"""
        id = 1
        b = Base()
        self.assertEqual(id, b.id)

    def test_base_id(self):
        """tests the id assigned at instantiation"""
        id = 12
        b = Base(12)
        self.assertEqual(id, 12)

    def test_dict_to_json_rect(self):
        """tests the dictionary to json method"""
        rect = Rectangle(1, 2, 3, 4, 5)
        res = Base.to_json_string([rect.to_dictionary()])
        exp = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        self.assertEqual(res, exp)

    def test_dict_to_json_sqr(self):
        """tests the dictionary to json method"""
        rect = Square(2, 3, 4, 5)
        res = Base.to_json_string([rect.to_dictionary()])
        exp = '[{"id": 2, "size": 3, "x": 4, "y": 5}]'
        self.assertEqual(res, exp)

    def test_dict_to_json_diff_types(self):
        """tests the dictionary to json method"""
        rect = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        sqr = Square(3, 4, 5, 6).to_dictionary()
        result = Base.to_json_string([rect, sqr])
        exp1 = '{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}'
        exp2 = '{"id": 3, "size": 4, "x": 5, "y": 6}'
        exp = '[{}, {}]'.format(exp1, exp2)
        self.assertEqual(res, exp)

    def test_dict_to_json_type_error(self):
        """tests the type error"""
        with self.assertRaises(TypeError):
            Base.to_json_string(0)
        with self.assertRaises(TypeError):
            Base.to_json_string([0, 1])

    def test_dict_to_json_empty_list(self):
        """tests the empty list for base"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")
        result = Base.to_json_string()
        self.assertEqual(result, "[]")

    def test_save_to_file(self):
        """tests the save to file method"""
        exp1 = '{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}'
        exp = '[{}, {}]'.format(exp1, exp1)
        rect = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        Rectangle.save_to_file([rect, rect])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), exp)

    def test_save_to_file_type_error(self):
        """tests the type error on base method"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([Rectangle(2, 3), Square(2)])
        with self.assertRaises(TypeError):
            Rectangle.save_to_file('str')

    def test_save_to_file_empty_list(self):
        """tests the save to file method"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('', file.read())
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('', file.read())

    def test_from_json_string(self):
        """tests the from json method"""
        json = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        result = [{id: 1, width: 2, height: 3, x: 4, y: 5}]
        self.assertEqual(Rectangle.from_json_string(json), result)

    def test_from_json_string_type_error(self):
        """tests for wrong input"""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string([])

    def test_from_json_string_empty_input(self):
        """test for empty input"""
        self.assertEqual(Rectangle.from_json_string(''), [])
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_create_instance(self):
        """test for creating an instance"""
        rect = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        sqr = Square(3, 4, 5, 6).to_dictionary()
        inst = Base.to
