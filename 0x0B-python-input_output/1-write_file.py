#!/usr/bin/python3
"""My write_file module

Contains the write_file function

"""


def write_file(filename="", text=""):
    """Write_file function
    Writes text to filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        written = f.write(text)
    return written
