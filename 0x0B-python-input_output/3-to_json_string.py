#!/usr/bin/python3
"""This module contains a function that returns the json of an obj"""


import json


def to_json_string(obj):
    """this function serializes an object"""
    return json.dumps(obj)
