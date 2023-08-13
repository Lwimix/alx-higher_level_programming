#!/usr/bin/python3
def print_list_integer(my_list=[]):
    counter = 0
    len_my_list = len(my_list)
    while counter < len_my_list:
        print("{}".format(my_list[counter]))
        counter = counter + 1
