#!/usr/bin/python3
"""This module contains a function that saves json to a file"""


import json


def save_to_json_file(my_obj, filename):
    """this function saves a json to a file"""
    try:
        with open(filename, mode='w', encoding='utf-8') as f:
            json.dump(my_obj, f)
    except Exception as e:
        raise TypeError("{} {}".format(my_obj, e))
