#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    count = 0
    len_outer_matrix = len(matrix)
    while counter < len_outer_matrix:
        len_matrix = len(matrix[counter])
        while count <  len_matrix:
            if count + 1 == len_matrix:
                print("{:d}".format(matrix[counter][count]))
                count = count + 1
            else:
                print("{:d}".format(matrix[counter][count]), end = " ")
                count = count + 1
        count = 0
        counter = counter + 1
    print("")
