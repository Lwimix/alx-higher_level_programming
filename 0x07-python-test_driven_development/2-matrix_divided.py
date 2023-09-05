#!/usr/bin/python3
"""My matrix addition module
Contains matrix_divided(), which divides a matrix
No importing done, no unique functions
Returns the divided matrix
"""


def matrix_divided(matrix, div):
    """Divides a matrix and returns the divided matrix
    matrix must be a list and div an integer(not zero)
    """
    msg = 'matrix must be a matrix (list of lists) of integers/floats'
    row_msg = 'Each row of the matrix must have the same size'
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    else:
        for item in matrix:
            if not isinstance(item, list):
                raise TypeError(msg)
            if len(item) != len(matrix[0]):
                raise TypeError(row_msg)
            for i in item:
                if not isinstance(i, int) and not isinstance(i, float):
                    raise TypeError(msg)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    new_matrix = [row[:] for row in matrix]
    for new_row in new_matrix:
        count = 0
        for i in new_row:
            new_row[count] = round(i / div, 2)
            count = count + 1
    return new_matrix
