#!/usr/bin/python3
"""This module contains a function that adds all args to a list
and saves them"""


import sys
import os
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
items = []
if os.path.isfile(filename):
    items = load_from_json(filename)
for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])
print(items)
save_to_json(items, filename)
