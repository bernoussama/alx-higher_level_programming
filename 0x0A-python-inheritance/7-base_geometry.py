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
            errormsg = "{} must be an integer".format(name)
            raise TypeError(errormsg)
        if value <= 0:
            errormsg = "{} must be greater than 0".format(name)
            raise ValueError()
