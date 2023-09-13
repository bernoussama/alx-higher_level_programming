#!/usr/bin/python3
def roman_to_int(roman_string):
    numeral = 0
    numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    substractive = ("IV", "IX", "XL", "XC", "CD", "CM")
    if isinstance(roman_string, str):
        for idx, char in enumerate(roman_string):
            if roman_string[idx : idx + 2] in substractive:
                numeral -= numerals[char]
            else:
                numeral += numerals[char]
    return numeral
