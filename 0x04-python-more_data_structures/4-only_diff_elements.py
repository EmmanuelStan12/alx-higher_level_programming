#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for item in set_1:
        if item not in set_2:
            result.append(item)
    for item in set_2:
        if item not in set_1:
            result.append(item)
    return {item for item in result}
