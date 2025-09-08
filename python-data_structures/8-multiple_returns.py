#!/usr/bin/python3

def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character"""
    length = len(sentence)
    if length == 0:
        first_character = None
    else:
        first_character = sentence[0]

    new_tuple = (length, first_character)
    return new_tuple


# sentence = "At school, I learnt C!"
# length, first = multiple_returns(sentence)
# print("Length: {:d} - First character: {}".format(length, first))
