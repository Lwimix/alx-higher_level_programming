#!/usr/bin/python3
"""My json object to file module

Contains save_to_json_file function

"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function
    Saves object to file using json representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
