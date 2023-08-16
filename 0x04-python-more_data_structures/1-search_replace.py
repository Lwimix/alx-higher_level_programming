#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy_list = my_list[:]
    count = 0
    for element in my_list:
        if search == cpy_list[count]:
            cpy_list[count] = replace
        else:
            count = count + 1
    return cpy_list
