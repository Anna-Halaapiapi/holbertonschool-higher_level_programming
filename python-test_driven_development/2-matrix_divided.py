#!/usr/bin/python3
"""
This module provides the matrix_divided function.
This function takes a matrix (list of lists) and a div (divider).
The function will divide each element of the matrix by the divider.
Returns a new matrix with the computed values.
Produces errors for invalid inputs.
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
    matrix: list of lists that must contain ints or floats
    div: int or float to divide the matrix by.

    Return:
    a new matrix
    """
    # check if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # check if each element in matrix is an int or float
    for row in matrix:
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError
                ("matrix must be a matrix (list of lists) of integers/floats")

    # check if all row lengths are the same
    check_row_len = set(map(len, matrix))
    if not len(check_row_len) == 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    row_length = len(matrix[0])

    # build new matrix with computed values
    for row in matrix:
        new_row = [] * row_length
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix


# matrix = [
#     [1, 2, 3],
#     [4, 5],
#     # [4, 4, 5, 6, 8]
# ]
# print(matrix_divided(matrix, 3))
# # # print(matrix)
