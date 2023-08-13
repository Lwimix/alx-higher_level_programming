#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list) - 1
    cpy_list = my_list
    while count >= 0:
        print("{}".format(cpy_list[count]))
        count = count - 1
