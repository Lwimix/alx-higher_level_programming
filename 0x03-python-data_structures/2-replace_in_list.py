#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    no_of_elements = len(my_list)
    cpy_list = my_list
    if idx < 0 | idx > no_of_elements:
        return my_list
    else:
        cpy_list[idx] = element
        return cpy_list
