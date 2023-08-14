#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if idx < 0 or idx >= len_list:
        return my_list
    else:
        next_idx = idx + 1
        my_list = my_list[:idx] + my_list[next_idx:]
        return my_list
