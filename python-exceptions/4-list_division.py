#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists
    Aegs:
    my_list_1: list 1 of any data type
    my_list_2: list 2 of any data type
    list_length: max length of lists 1 or 2

    Return:
    a new list of list_length with all divisions"""
    i = 0
    new_list = []
    while (i < list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
        i = i + 1
    return new_list
