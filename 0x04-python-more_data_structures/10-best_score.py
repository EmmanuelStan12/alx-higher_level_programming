#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    max = 0
    key = ''
    if a_dictionary is None:
        return None
    for k, v in a_dictionary.items():
        if i == 0 or a_dictionary[k] > max:
            max = a_dictionary[k]
            key = k
        i = i + 1
    if i == 0:
        return None
    return key
