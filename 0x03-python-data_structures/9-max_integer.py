#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return None
    biggest = my_list[0]
    counter = 1
    while counter < len_list:
        if my_list[counter] > biggest:
            biggest = my_list[counter]
            counter = counter + 1
        else:
            counter = counter + 1
    return biggest
