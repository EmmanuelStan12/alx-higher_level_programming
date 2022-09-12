#!/usr/bin/python

def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
