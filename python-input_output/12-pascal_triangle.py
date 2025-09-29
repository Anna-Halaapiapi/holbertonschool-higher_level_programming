#!/usr/bin/python3
"""
This module provides the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n.
    Args:
    n = row length
    """
    if n <= 0:
        return []

    p_tri = [[1]]
    i = 1
    # outer loop to build rows
    while i < n:
        
        # start with new row of length i
        new_row = [0] * (i + 1)

        # access prev row for inner loop calcs
        prev_row = p_tri[i - 1]

        # reset inner loop counters
        j = 0

        # inner loop to build columns
        while j < len(new_row):
            # handle 1 at start of list
            if j == 0:
                new_row[j] = 1

            # handle 1 at end of list
            elif j == len(new_row) - 1:
                new_row[j] = 1
            
            else:
                # handle middle of list (not start or end)
                new_row[j] = prev_row[j - 1] + prev_row[j]

            j += 1
        # add new row to triangle
        p_tri.append(new_row)

        i += 1

    return p_tri
