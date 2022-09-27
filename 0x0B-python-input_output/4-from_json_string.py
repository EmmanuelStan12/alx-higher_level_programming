#!/usr/bin/python3
"""This module contains a function that converts a string to pyObject"""


import json


def from_json_string(my_str):
    """this function that converts a string a pyObject"""
    return json.loads(my_str)
