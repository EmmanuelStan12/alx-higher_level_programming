#!/usr/bin/python3
"""
This module contains a function that prints your name in
given format
"""


def say_my_name(first_name, last_name=""):
    """
    this function prints out your name in a given format
    """
    sep = ", "
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    if len(last_name.strip()) == 0:
        sep = " "
        last_name = last_name.strip()
    if len(first_name.strip()) == 0:
        sep = ""
        first_name = first_name.strip()
    print("My name is {}{}{}".format(first_name, sep, last_name))
