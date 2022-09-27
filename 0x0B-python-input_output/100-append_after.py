#!/usr/bin/python3
"""This module contains a function that appends a string
after a search string"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a new line after each successful search"""
    with open(filename, mode="r", encoding='utf-8') as f:
        data = f.readlines()

    for i in range(len(data)):
        if search_string in data[i]:
            data.insert(i + 1, new_string)

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write('')
    with open(filename, mode='a', encoding='utf-8') as f:
        for line in data:
            f.write(''.join(line))
