#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for i in range(len(list)):
            space = ' '
            if i == len(list) - 1:
                space = ''
            print("{:d}".format(list[i]), end=space)
        print("")
