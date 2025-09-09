#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a Roman numeral to an integer
    Arg:
    roman_string: the roman numeral to convert
    Return:
    the converted integer or
    0 if roman_string is not a string or None
    """
    # dictionary of all poss keys & values
    roman_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000, "XC": 90}
    # check if roman string None
    if roman_string is None:
        return 0

    # check if string is not a string
    if not isinstance(roman_string, str):
        return 0

    # check if roman string is preexisting in dict
    if roman_string in roman_dict:
        result = roman_dict[roman_string]
        return result

    # # build number if doesn't already exist in dictionary
    # # outer loop - chars in string
    # # inner loop - check roman dictionary
    else:
        str_length = len(roman_string)
        result = 0
        i = 0
        while i < str_length:
            if roman_string[i] == 'I' and i < str_length - 1:
                next_char = roman_string[i + 1]
                # handle special 'IV' and 'IX' within string
                if next_char == 'V':
                    result = result + roman_dict['IV']
                    i = i + 2
                    continue

                if next_char == 'X':
                    result = result + roman_dict['IX']
                    i = i + 2
                    continue

            if roman_string[i] == 'X' and i < str_length - 1:
                next_char = roman_string[i + 1]
                # handle special 'XC' within string
                if next_char == 'C':
                    result = result + roman_dict['XC']
                    i = i + 2
                    continue

            # handle normal numerals
            if roman_string[i] in roman_dict:
                result = result + roman_dict[roman_string[i]]
            i = i + 1
        return result


# roman_number = "XCIX"
# print("{} = {}".format(roman_number, roman_to_int(roman_number)))
