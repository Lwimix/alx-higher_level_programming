#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = 0
    cpy_list = my_list[:]
    cpy_list = set(cpy_list)
    cpy_list = list(cpy_list)
    for item in cpy_list:
        added = added + item
    return added
