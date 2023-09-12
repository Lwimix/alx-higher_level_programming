#!/usr/bin/python3
"""My append_write module

Contains the append_write function

"""


def append_write(filename="", text=""):
    """Append_write function
    Appends text to filename
    """
    with open(filename, 'a', encoding='utf-8') as f:
        written = f.write(text)
    return written
