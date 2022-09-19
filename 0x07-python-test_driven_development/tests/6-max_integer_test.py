#!/usr/bin/python3
"""
this module contains a function that checks for the largest int in a list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The test implementation class"""

    def test_positive_1(self):
        """
        Tests for a max int in a list
        """
        list = [1, 3, 4, 5, 6]
        max = 6
        self.assertEquals(max_integer(list), max)

    def test_positive_2(self):
        """
        Tests for a max int in a list
        """
        list = [6]
        max = 6
        self.assertEquals(max_integer(list), max)

    def test_empty_list(self):
        """
        Tests for a max int in a list
        """
        list = []
        max = None
        self.assertEquals(max_integer(list), max)

    def test_negative_1(self):
        """
        Tests for a max int in a list
        """
        list = [-1, -3, -4, -5, -6]
        max = -1
        self.assertEquals(max_integer(list), max)

    def test_negative_2(self):
        """
        Tests for a max int in a list
        """
        list = [-1]
        max = -1
        self.assertEquals(max_integer(list), max)
