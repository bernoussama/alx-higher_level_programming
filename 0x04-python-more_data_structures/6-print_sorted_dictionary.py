#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())
    for item in sorted_dict:
        print(f"{item}: {a_dictionary[item]}")
