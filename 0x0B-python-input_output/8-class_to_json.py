#!/usr/bin/python3
"""The class to json module

Converts a class and its attributes to json

"""
import json


def class_to_json(obj):
    """class_to_json function
    Converts class to json
    """
    attrib = vars(obj)
    json_attrib = {}
    for key, value in attrib.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_attrib[key] = value
    return json_attrib
