#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    i = 0
    ret_list = [None] * list_length
    try:
        while (i < list_length):
            try:
                ret_list[i] = (my_list_1[i] / my_list_2[i])
                i = i + 1
            except (TypeError, ZeroDivisionError, IndexError) as b:
                ret_list[i] = 0
                i = i + 1
                if (isinstance(b, TypeError)):
                    print("wrong type")
                if (isinstance(b, ZeroDivisionError)):
                    print("division by 0")
                if (isinstance(b, IndexError)):
                    print("out of range")
                pass
    finally:
        return ret_list
