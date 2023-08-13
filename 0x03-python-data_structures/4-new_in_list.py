#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list[:]
    len_list = len(my_list)
    if idx < 0:
        return cpy_list
    else:
        cpy_list[idx] = element
        return cpy_list
