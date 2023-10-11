#!/usr/bin/python3
"""
    BaseGeometry module

"""


class BaseGeometry:
    """
    empty class BaseGeometry
    """

    def area(self):
        """functoin area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function integer_validator"""
        if isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
