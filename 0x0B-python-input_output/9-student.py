#!/usr/bin/python3
"""My student class module

Contains the student class

"""


class Student():
    """Student class
    Has attributes of student

    Methods:
    __init__(self, first_name, last_name, age):
    def to_json(self):
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class_to_json function
        Converts class to json
        """
        attrib = vars(self)
        json_attrib = {}
        for key, value in attrib.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_attrib[key] = value
        return json_attrib
