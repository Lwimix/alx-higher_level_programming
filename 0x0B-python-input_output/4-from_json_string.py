#!/usr/bin/python3
import json
"""My reverse json module

Contains from_json_string function

"""


def from_json_string(my_str):
    """from_json_string function
    Converts from json string back to data structure
    """
    returned = json.loads(my_str)
    return returned
