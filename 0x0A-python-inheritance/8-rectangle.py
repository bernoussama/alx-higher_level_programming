#!/usr/bin/python3
"""
    Rectangle module

"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    extends BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validation("width", width)
        self.integer_validation("height", height)
        self.__width = width
        self.__height = height
