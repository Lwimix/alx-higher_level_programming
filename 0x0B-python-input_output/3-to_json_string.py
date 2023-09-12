#!/usr/bin/python3
"""My json_string module

Contains to_json_string function

"""
import json


def to_json_string(my_obj):
    """to_json_string function
    Converts object to json string
    """
    converted = json.dumps(my_obj)
    return converted
