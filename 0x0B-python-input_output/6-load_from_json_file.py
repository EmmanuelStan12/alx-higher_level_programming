#!/usr/bin/python3
"""This module contains a function that creates object from JSON file"""


import json


def load_from_json_file(filename):
    """this function creats an object from a file"""
    str = ""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
    #try:
    #    result = json.loads(str)
    #except Exception as e:
    #    raise ValueError(e)
    #return result
