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

    def to_json(self, attrs=None):
        """class_to_json function
        Converts class to json
        """
        attrib = vars(self)
        json_attrib = {}
        for key, value in attrib.items():
            if isinstance(value, (list, dict, str, int, bool)):
                if isinstance(attrs, list):
                    for item in attrs:
                        if not isinstance(item, str):
                            break
                        if item in attrib.keys():
                            json_attrib[item] = attrib[item]
                else:
                    json_attrib[key] = value
        sorted_attrib = dict(sorted(json_attrib.items()))
        return sorted_attrib

    def reload_from_json(self, json):
        """reload_from_json function
        Replaces all attributes of Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
