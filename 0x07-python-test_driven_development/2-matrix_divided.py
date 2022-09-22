#!/usr/bin/python3
"""
this module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    this function divides all elements of a matrix by
    the div variable
    """
    list_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if type(matrix) != list:
        raise TypeError(list_msg)
    if len(matrix) == 0:
        raise TypeError(list_msg)
    row_len = None
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(list_msg)
        for item in matrix[i]:
            if type(item) != int and type(item) != float:
                raise TypeError(list_msg)
        if i == 0:
            row_len = len(matrix[i])
            continue
        if row_len != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in range(len(row)):
            new_row.append(round(row[i] / div, 2))
        new_matrix.append(new_row)
    return new_matrix
