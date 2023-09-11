#!/usr/bin/python3
"""My Lookup Module

Contains lookup function

"""


def lookup(obj):
    """My lookup function
    Checks the available attributes and methods of an obj
    """
    return dir(obj)
