#!/usr/bin/python3
"""this module tests the base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """this class tests the base class"""
    
    def test_base_default_id(self):
        """tests the id assigned to the class"""
        id = 1
        b = Base()
        self.assertEquals(id, b.id)

    def test_base_id(self):
        """tests the id assigned at instantiation"""
        id = 12
        b = Base(12)
        self.assertEquals(id, 12)
