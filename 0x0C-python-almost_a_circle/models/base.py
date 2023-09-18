#!/usr/bin/python3
"""Module with a class

Contains my base class

"""
import json


class Base():
    """Base class
    Base class of all classes

    Methods:
    __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string static method
        Converts object to JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        my_json = json.dumps(list_dictionaries)
        return my_json

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file class method
        Saves json string to file
        """
        if list_objs is None:
            list_objs = []
        class_name = str(cls.__name__) + ".json"
        convert = []
        for obj in list_objs:
            convert.append(obj.to_dictionary())
        my_json = cls.to_json_string(convert)
        with open(class_name, 'w') as f:
            f.write(my_json)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string static method
        Converts JSON string to object
        """
        if json_string is None or len(json_string) == 0:
            return []
        my_obj = json.loads(json_string)
        return my_obj

    @classmethod
    def create(cls, **dictionary):
        """create class method
        Returns instance with set attributes
        """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """load_from_file class method
        Returns a list of instances
        """
        class_name = str(cls.__name__) + ".json"
        try:
            with open(class_name, 'r') as f:
                info_string = f.read()
                real_info = cls.from_json_string(info_string)
                instances = []
                for item in real_info:
                    instance = cls.create()
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
