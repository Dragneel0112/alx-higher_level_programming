#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dictionary = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_dictionary[roman_string[j]] \
                 > roman_dictionary[roman_string[j - 1]]:
            roman_num += roman_dictionary[roman_string[j]] - 2 * \
                        roman_dictionary[roman_string[j - 1]]
        else:
            roman_num += roman_dictionary[roman_string[j]]
    return roman_num
