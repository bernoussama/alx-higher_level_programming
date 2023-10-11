#!/usr/bin/python3
"""
class_to_json module
returns dictionary description of object for JSON serialization
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object

    """
    return obj.__dict__
