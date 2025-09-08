#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of ints"""
    # outer loop for row
    for row in matrix:
        index = 0
        # inner loop for column
        for element in row:
            print("{:d}".format(element), end='')
            if index < len(row) - 1:
                print(" ", end='')
            index = index + 1
        print()

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()
