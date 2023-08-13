#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Reverse lists"""
    cpy_list = my_list[::-1]
    for item in cpy_list:
        print("{}".format(item))
