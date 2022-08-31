#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for item_1 in set_1:
        for item_2 in set_2:
            if item_2 == item_1:
                result.append(item_1)
    return result
