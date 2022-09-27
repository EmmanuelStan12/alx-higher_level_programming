#!/usr/bin/python3
"""This module contains a function that appends a string
after a search string"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a new line after each successful search"""
    with open(filename, mode="r", encoding='utf-8') as f:
        data = f.readlines()

    for i in range(len(data)):
        if data[i].find(search_string) != -1:
            data.insert(i + 1, new_string)

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(''.join(data))
