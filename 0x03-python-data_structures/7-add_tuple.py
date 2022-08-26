#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    elem_a_1 = 0
    elem_a_2 = 0
    elem_b_1 = 0
    elem_b_2 = 0
    if len(tuple_a) == 1:
        elem_a_1 = tuple_a[0]
    elif len(tuple_a) > 1:
        elem_a_1 = tuple_a[0]
        elem_a_2 = tuple_a[1]
    if len(tuple_b) == 1:
        elem_b_1 = tuple_b[0]
    elif len(tuple_b) > 1:
        elem_b_1 = tuple_b[0]
        elem_b_2 = tuple_b[1]
    elem_a = elem_a_1 + elem_b_1
    elem_b = elem_a_2 + elem_b_2
    return (elem_a, elem_b)
