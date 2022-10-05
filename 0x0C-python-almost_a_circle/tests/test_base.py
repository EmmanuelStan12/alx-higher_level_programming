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
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(1, b.id)
        Base._Base__nb_objects = 4
        a = Base()
        self.assertEqual(5, a.id)
        Base._Base__nb_objects = 20
        c = Base()
        self.assertEqual(21, c.id)

    def test_base_id(self):
        """tests the id assigned at instantiation"""
        id = 12
        b = Base(12)
        self.assertEqual(id, 12)

    def test_dict_to_json_rect(self):
        """
        tests the dictionary to json functionality with rectangle class
        """
        rect = Rectangle(1, 2, 3, 4, 5)
        res = Base.to_json_string([rect.to_dictionary()])
        exp = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        self.assertEqual(res, exp)

    def test_dict_to_json_sqr(self):
        """
        tests the dictionary to json functionality with square class
        """
        rect = Square(2, 3, 4, 5)
        res = Base.to_json_string([rect.to_dictionary()])
        exp = '[{"id": 5, "size": 2, "x": 3, "y": 4}]'
        self.assertEqual(res, exp)

    def test_dict_to_json_diff_types(self):
        """tests the dictionary to json method with different types"""
        rect = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        sqr = Square(4, 5, 6, 3).to_dictionary()
        result = Base.to_json_string([rect, sqr])
        exp1 = '{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}'
        exp2 = '{"id": 3, "size": 4, "x": 5, "y": 6}'
        exp = '[{}, {}]'.format(exp1, exp2)
        self.assertEqual(result, exp)

    def test_dict_to_json_type_error(self):
        """tests the type error for dictionary conversion"""
        with self.assertRaises(TypeError):
            Base.to_json_string(0)
        with self.assertRaises(TypeError):
            Base.to_json_string([0, 1])

    def test_dict_to_json_empty_list(self):
        """tests the empty list for to convert to json string"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_save_to_file(self):
        """tests saving json to file"""
        exp1 = '{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}'
        exp = '[{}, {}]'.format(exp1, exp1)
        rect = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rect, rect])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), exp)

    def test_save_to_file_type_error(self):
        """tests the exception thrown with invalid arguments"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([Rectangle(2, 3), Square(2)])
        with self.assertRaises(TypeError):
            Rectangle.save_to_file('str')

    def test_save_to_file_empty_list(self):
        """tests the save json to a file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('', file.read())
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('', file.read())

    def test_from_json_string(self):
        """tests to convert json strings to dictionaries"""
        json = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        result = [{'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}]
        self.assertEqual(Rectangle.from_json_string(json), result)

    def test_from_json_string_type_error(self):
        """tests for wrong input that raises type error"""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string([])

    def test_from_json_string_empty_input(self):
        """test for converting json string with empty input"""
        self.assertEqual(Rectangle.from_json_string(''), [])
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_create_instance(self):
        """test for creating an instance"""
        rect = Rectangle.create(id=1, width=2, height=5, x=5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 5)

    def test_create_instance_with_wrong_params(self):
        """test for creating an instance with wrong parameters"""
        rect = Rectangle.create(id=1, width=2, height=5, z=5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 5)
        with self.assertRaises(AttributeError):
            rect.z

    def test_create_instance_invalid_type(self):
        """test for creating an instance with invalid type"""
        with self.assertRaises(TypeError):
            rect = Rectangle.create('x')

    def test_file_to_instances(self):
        """tests for creating instances from file"""
        exp1 = '{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}'
        exp = '[{}, {}]'.format(exp1, exp1)
        rect = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rect, rect])
        instances = Rectangle.load_from_file()
        self.assertEqual(type(instances), list)
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, rect.id)
        self.assertEqual(instances[1].id, rect.id)

    def test_file_to_instances_file_not_exists(self):
        """
        tests for creating instances when file does not exist
        """
        Rectangle.save_to_file([])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 0)
        self.assertEqual(instances, [])

    def test_save_from_file_csv_with_diff_types(self):
        """
        tests for saving to csv file from dictionary with diff types
        """
        rect = Rectangle(1, 2, 3, 4, 5)
        sqr = Square(1, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([rect, sqr])

    def test_save_and_load_from_file_csv_with_empty_list(self):
        """
        tests for saving to csv file from dictionary with empty list
        """
        Rectangle.save_to_file_csv([])
        result = Rectangle.load_from_file_csv()
        self.assertEqual(result, [])

    def test_save_from_file_csv_with_wrong_input(self):
        """
        tests for saving to csv file from dictionary with wrong types
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(['str'])

    def test_save_and_load_from_csv_file_rect(self):
        """
        tests for saving and loading from csv file
        """
        r1 = Rectangle(10, 7, 2, 8, 6)
        r2 = Rectangle(2, 4, 3, 4, 6)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles_output), 2)
        self.__rect_instances(r1, list_rectangles_output[0])
        self.__rect_instances(r2, list_rectangles_output[1])

    def __rect_instances(self, rect1, rect2):
        """
        tests for equality with two rectangles
        """
        self.assertEqual(rect1.x, rect2.x)
        self.assertEqual(rect1.y, rect2.y)
        self.assertEqual(rect1.width, rect2.width)
        self.assertEqual(rect1.height, rect2.height)
        self.assertEqual(rect1.id, rect2.id)

    def test_save_and_load_from_csv_file_sqr(self):
        """
        tests for saving and loading from csv file
        """
        s1 = Square(10, 6, 7, 9)
        s2 = Square(3, 4, 5, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(len(list_squares_output), 2)
        self.__sqr_instances(s1, list_squares_output[0])
        self.__sqr_instances(s2, list_squares_output[1])

    def __sqr_instances(self, s1, s2):
        """
        tests for equality with two rectangles
        """
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.id, s2.id)


if __name__ == '__main__':
    unittest.main()
