#!/usr/bin/python3
"""
inherits_from module

"""


def inherits_from(obj, a_class):
    """
    function that returns:
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class;
    otherwise False.
    """
    obj_class = type(obj)
    return False if type(obj) is a_class else issubclass(obj_class, a_class)
