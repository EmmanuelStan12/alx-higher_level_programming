#!/usr/bin/python3
"""
this module has a function that does some text indentation a special characters.
"""


def text_indentation(text):
    """
    this function does text indentation for special characters
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    new_line = False
    for c in text:
        if new_line and c.isspace():
            continue
        else:
            new_line = False
            print(c, end='')
        if c == '?' or c == '.' or c == ':':
            print('\n')
            new_line = True
