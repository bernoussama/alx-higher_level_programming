#!/usr/bin/python3
"""class_to_json module

"""


def class_to_json(obj):
    """function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object

    """
    # Check if the object is a dictionary, list, string, integer, or boolean
    if isinstance(obj, dict):
        # If it's a dictionary, recursively serialize its values
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        # If it's a list, recursively serialize its elements
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, (str, int, bool)):
        # If it's a string, integer, or boolean, return it as is
        return obj
    elif hasattr(obj, "__dict__"):
        # For custom classes, serialize the __dict__ attribute
        return class_to_json(obj.__dict__)
    else:
        raise ValueError(f"Unsupported data type: {type(obj)}")
