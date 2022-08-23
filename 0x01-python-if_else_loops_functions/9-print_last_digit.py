#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    mod = n if not n else -(n - 10) if number < 0 else n
    print(mod, end = '')
    return mod
