#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    keys = list(a_dictionary.keys())
    cpy_a_dict = a_dictionary.copy()
    for item in keys:
        if item == key:
            a_dictionary[key] = value
            return cpy_a_dict
    cpy_a = list(a_dictionary.items())
    new_value = (key, value)
    cpy_a.append(new_value)
    cpy_a = dict(cpy_a)
    return cpy_a
