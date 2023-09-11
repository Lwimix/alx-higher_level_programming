#!/usr/bin/python3
"""My is_kind_of_class module

Contains is_kind_of_class function

"""


def is_kind_of_class(obj, a_class):
    """The is_kind_of_class function
    Checks if obj instance or inherited
    """
    if isinstance(obj, a_class):
        return True
    return False
