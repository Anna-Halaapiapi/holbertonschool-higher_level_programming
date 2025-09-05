#!/usr/bin/python3

def remove_char_at(str, n):
    str_len = len(str)
    str_copy = []
    i = 0

    while (i < str_len):
        if (i == n):
            i = i + 1
            continue

        str_copy.append(str[i])
        i = i + 1

    return (''.join(str_copy))
