#!/usr/bin/python3
"""My read_file module

Contains read_file function

"""


def read_file(filename=""):
    """Read_file function
    Reads the contents of a file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for item in f.readlines():
            print(item, end="")
