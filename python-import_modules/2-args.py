#!/usr/bin/python3

import sys
if __name__ == "__main__":
    # find number of args
    n = len(sys.argv) - 1

    # 0 args passed
    if n == 0:
        print("{} arguments.".format(n))

    # 1 arg passed
    elif n == 1:
        print("1 argument:\n1: {}".format(sys.argv[1]))

    # 2+ args passed
    else:
        print("{} arguments:".format(n))

        for i in range(1, n + 1):
            print("{0}: {1}".format(i, sys.argv[i]))
