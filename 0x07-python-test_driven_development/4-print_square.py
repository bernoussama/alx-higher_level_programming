#!/usr/bin/python3

"""
This the "4-print_square" module, Example,

>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    funtion that prints squre of "#" of size "size"

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    print("\n".join(["#" * size for _ in range(size)]))
