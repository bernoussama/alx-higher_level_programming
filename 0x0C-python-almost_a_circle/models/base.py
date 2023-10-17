#!/usr/bin/python3
"""
base module
"""
import json
from os import write


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string method"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file method"""
        objs = []
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as f:
                json.dump(objs, f)
            return

        for obj in list_objs:
            objs.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as f:
            json.dump(objs, f)
