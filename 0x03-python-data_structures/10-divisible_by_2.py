#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = (my_list[:])
    len_list = len(my_list)
    counter = 0
    while counter < len_list:
        if my_list[counter] % 2 == 0:
            new_list[counter] = True
            counter = counter + 1
        else:
            new_list[counter] = False
            counter = counter + 1
    final_list = tuple(new_list)
    return final_list
