#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n = len(sys.argv)
    result = 0

for i in range(1, n):
    result = result + int(sys.argv[i])

print("{}".format(result))
