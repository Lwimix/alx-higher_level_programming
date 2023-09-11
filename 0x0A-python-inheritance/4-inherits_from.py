#!/usr/bin/python3
"""My inherits_from module

Contains inherits_from function

"""


def inherits_from(obj, a_class):
    """The is_kind_of_class function
    Checks if obj instance or inherited
    """
    if isinstance(obj, a_class) and (type(obj) is not a_class):
        return True
    return False
