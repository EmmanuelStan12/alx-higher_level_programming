#!/usr/bin/python3
"""This module contains a class that inherits from lists"""


class MyList(list):
    """This class inherits list class"""

    def print_sorted(self):
        """this function prints all elements of the list in sorted form"""
        print(sorted(self))
