#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys = sorted(keys)
    for item in keys:
        print("{}: {}".format(item, a_dictionary[item]))
