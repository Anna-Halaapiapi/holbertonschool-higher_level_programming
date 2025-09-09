#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a Roman numeral to an integer
    Arg:
    roman_string: the roman numeral to convert
    Return:
    the converted integer or
    0 if roman_string is not a string, empty or None
    """
    # dictionary of all poss keys & values
    roman_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    # check if roman string None or empty
    if roman_string is None or "":
        return 0

    # check if string is not a string
    if not isinstance(roman_string, str):
        return 0

    # check if roman string is preexisting in dict
    if roman_string in roman_dict:
        number = roman_dict[roman_string]
        return number

    # # build number if doesn't already exist in dictionary
    # # outer loop - chars in string
    # # inner loop - check roman dictionary
    else:
        number = 0
        for char in roman_string:
            for key, value in roman_dict.items():
                if char in roman_dict:
                    number = number + roman_dict[char]
                    break
        return number


# roman_number = "XII"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))
