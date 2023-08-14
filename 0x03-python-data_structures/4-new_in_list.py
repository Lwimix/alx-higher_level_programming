#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list[:]
    new_cpy_list = my_list
    len_list = len(my_list)
    if idx < 0 or idx >= len_list:
        return new_cpy_list
    else:
        cpy_list[idx] = element
        return cpy_list
