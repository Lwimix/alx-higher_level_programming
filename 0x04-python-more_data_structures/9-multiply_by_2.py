#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    values = list(a_dictionary.values())
    cpy_a_dict = a_dictionary.copy()
    values = [value * 2 for value in values]
    keys = list(a_dictionary.keys())
    len_keys = len(keys)
    count = 0
    while count < len_keys:
        cpy_a_dict[keys[count]] = values[count]
        count = count + 1
    return cpy_a_dict
