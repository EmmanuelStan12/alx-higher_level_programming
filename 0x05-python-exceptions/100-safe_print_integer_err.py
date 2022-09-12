#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as exp:
        print("Exception: {}".format(exp))
        return False
    else:
        return True
