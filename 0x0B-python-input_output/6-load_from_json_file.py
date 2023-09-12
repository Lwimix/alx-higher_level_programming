#!/usr/bin/python3
import json
"""The load json module

Contains load_from_json_file function

"""


def load_from_json_file(filename):
    """load_from_json_file function
    Creates an Object from a JSON file
    """
    with open(filename, 'r') as f:
        loads = json.load(f)
    return loads
