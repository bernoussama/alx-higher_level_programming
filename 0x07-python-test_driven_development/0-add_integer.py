#!/usr/bin/python3
""" 
this is  the "0-add_integer" module.

supplying one function add_integer(). Example,

>>> add_integer(5,5)
10
"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats
    Args:
    a : int|float
    b : int|float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
