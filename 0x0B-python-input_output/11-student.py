#!/usr/bin/python3
"""student module

"""


class Student:
    """class Student that defines a student by:

    Public instance attributes:
        @first_name
        @last_name
        @age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that returns the dictionary description
        with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of student instance

        """
        attributes = dict(self.__dict__)
        if isinstance(attrs, list):
            if all(isinstance(item, str) for item in attrs):
                for attr in self.__dict__.keys():
                    if attr not in attrs:
                        del attributes[attr]
                return attributes

        return attributes

    def reload_from_json(self, json):
        """
         replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
        """
        for key, value in json.items():
            self.__setattr__(key, value)
