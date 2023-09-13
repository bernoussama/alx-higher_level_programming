#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        to_delete = list()
        for k, v in a_dictionary.items():
            if v == value:
                to_delete.append(k)
        if len(to_delete) > 0:
            for k in to_delete:
                del a_dictionary[k]
