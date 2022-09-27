#!/usr/bin/python3
"""This module contains a function that reads a file"""


def read_file(filename=""):
    """this function reads a file"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
