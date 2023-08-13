#!/usr/bin/python3
def no_c(my_str):
    final_str = ""
    set_final = 0
    counter = 0
    len_my_str = len(my_str)
    while counter < len_my_str:
        if my_str[counter] == "c" or my_str[counter] == "C":
            counter = counter + 1
        else:
            if counter == 0:
                final_str = my_str[counter]
                set_final = 1
                counter = counter + 1
            else:
                if set_final == 0:
                    final_str = my_str[counter]
                    set_final = 1
                    counter = counter + 1
                else:
                    final_str = final_str + my_str[counter]
                    counter = counter + 1
    return final_str
