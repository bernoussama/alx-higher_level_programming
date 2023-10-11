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
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}

    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]

    elif isinstance(obj, (str, int, bool)):
        return obj

    elif hasattr(obj, "__dict__"):
        return class_to_json(obj.__dict__)
