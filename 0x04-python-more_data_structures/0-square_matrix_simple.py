#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    count = 0
    cpy_matrix = []
    counter = 0
    len_matrix = len(matrix)
    while counter < len_matrix:
        len_in_matrix = len(matrix[counter])
        row = []
        while count < len_in_matrix:
            row.append(matrix[counter][count] ** 2)
            count = count + 1
        cpy_matrix.append(row)
        count = 0
        counter = counter + 1
    return cpy_matrix
