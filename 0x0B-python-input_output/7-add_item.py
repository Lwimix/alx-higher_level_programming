#!/usr/bin/python3
"""My add_item module

Adds arguments to list then saves to add_item.json

"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def my_func():
    """My main function
    Does most of the heavy lifting
    """
    buf = []
    for item in sys.argv:
        if (item == sys.argv[0]):
            continue
        buf.append(item)
    save_to_json_file(buf, "add_item.json")
    loading = load_from_json_file("add_item.json")


if __name__ == '__main__':
    my_func()
