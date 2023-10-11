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
        if attrs is not None:
            for attr in self.__dict__.keys():
                if attr not in attrs:
                    del attributes[attr]
            return attributes

        return attributes
