#!/usr/bin/python3
def element_at(my_list, idx):
    len_my_list = len(my_list)
    if idx < 0 | idx > len_my_list:
        return None
    else:
        return my_list[idx]
