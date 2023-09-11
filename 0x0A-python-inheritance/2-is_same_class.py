#!/usr/bin/python3
"""My is_same_class module

Contains is_same_class function

"""
def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    return False
