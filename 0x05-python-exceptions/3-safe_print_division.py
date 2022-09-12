#!/usr/bin/python

def safe_print_division(a, b):

    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        result = None
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
