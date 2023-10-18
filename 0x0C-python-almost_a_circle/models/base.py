#!/usr/bin/python3
"""
base module
"""
import json


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
        """save to file class method"""
        objs = []
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as f:
                json.dump(objs, f)
            return

        for obj in list_objs:
            objs.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """from json string static method"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create class method"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """load from file class method"""
        dicts = ""
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                dicts = f.read()

        except FileExistsError:
            return []

        dicts = cls.from_json_string(dicts)
        if dicts == []:
            return []

        instances = []
        for obj in dicts:
            instances.append(cls.create(**obj))

        return instances
