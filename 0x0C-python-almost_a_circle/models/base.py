#!/usr/bin/python3
"""
base module
"""


class Base:
    """
    Base class
    with auto-incrementing ID
    """

    __nb_objects = 0

    def __init__(self, id=None):
        # self.validate_id(id)
        if id is not None:
            self.id = id
            return
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
