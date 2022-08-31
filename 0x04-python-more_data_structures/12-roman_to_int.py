#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {
            'M': 1000,
            'C': 100,
            'X': 10,
            'D': 500,
            'I': 1,
            'L': 50,
            'V': 5
        }
    value = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    i = 0
    while i < len(roman_string):
        if roman_string[i] in numerals.keys():
            current = numerals[roman_string[i]]
            if i + 1 < len(roman_string):
                next = numerals[roman_string[i+1]]
                if next > current:
                    current = next - current
                    i = i + 1
            value = value + current
            i = i + 1
        else:
            return 0
    return value
