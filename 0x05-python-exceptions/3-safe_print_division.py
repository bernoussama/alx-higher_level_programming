#!/usr/bin/python3
def safe_print_division(a, b):
    value = None
    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        print("Inside result: {:}".format(value))
        return value
