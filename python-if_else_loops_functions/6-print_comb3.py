#!/usr/bin/python3
for i in range(0, 10):

    for j in range(0, 10):
        if (i == 8) and (j == 9):
            break
        if (j != i) and (j != 0) and (i < j):
            print("{0}{1}, ".format(i, j), end='')
print("{}{}".format(8, 9), end='')
