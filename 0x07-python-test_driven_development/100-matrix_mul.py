#!/usr/bin/python3
"""this module contains a funtion that does matrix multiplication"""


def check_matrix(matrix, name):
    if type(matrix) != list:
        raise TypeError("{} must be a list".format(name))
    if len(matrix) == 0:
        raise ValueError("{} can't be empty".format(name))
    prev_row = None
    for row in matrix:
        if type(row) != list:
            raise TypeError("{} must be a list of lists".format(name))
        if len(row) == 0:
            raise ValueError("{} can't be empty".format(name))
        for elem in row:
            if type(elem) != int and type(elem) != float:
                raise TypeError("{} should contain only integers or floats".format(name))
        if prev_row != None:
            if len(prev_row) != len(row):
                raise TypeError("each row of {} must be of the same size".format(name))
        prev_row = row
    return (len(prev_row), len(matrix))

def matrix_mul(m_a, m_b):
    """
    this function does matrix multiplication
    """
    a_cols, a_rows = check_matrix(m_a, 'm_a')
    b_cols, b_rows = check_matrix(m_b, 'm_b')
    if b_rows != a_cols:
        raise ValueError("m_a and m_b can't be multiplied")
    # a_rows * b_cols
    # print("result: {} x {}".format(a_rows, b_cols))
    result = []
    for i in range(a_rows):
        row = []
        # print("i: {}, value: {}".format(i, m_a[i]))
        for j in range(b_cols):
            r_mul = 0
            for k in range(b_rows):
                # print("k: {}, j: {}, value: {}".format(k, j, m_b[k][j]))
                a = m_a[i][k] * m_b[k][j]
                r_mul += a
            row.append(r_mul)
        result.append(row)
    return result

