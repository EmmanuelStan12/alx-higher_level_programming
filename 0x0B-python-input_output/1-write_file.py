#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """this function reads a file"""
    with open(filename, mode="w", encoding='utf-8') as f:
        bytes = f.write(text)
    return bytes
