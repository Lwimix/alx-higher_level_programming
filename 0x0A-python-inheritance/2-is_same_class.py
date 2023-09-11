#!/usr/bin/python3
"""My is_same_class module

Contains is_same_class function

"""


def is_same_class(obj, a_class):
    """Is_same_class function
    Checks if class is the same
    """
    if type(obj) is a_class:
        return True
    return False
