#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    for item in matrix:
        print(*matrix[counter])
        counter = counter + 1
