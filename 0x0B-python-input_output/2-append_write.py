#!/usr/bin/python3
"""This module contains a function that appends content to a file"""


def append_write(filename="", text=""):
    """this function appends content to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        bytes = f.write(text)
    return bytes
