#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value.

    Args:
    a_dictionary: original dictionary.

    Return: key for max value or None if dict is None.
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_value = max(a_dictionary.values())

    for key, value in a_dictionary.items():
        if value == max_value:
            return key


# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
