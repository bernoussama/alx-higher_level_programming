#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx > 0 and idx < len(my_list):
        new_list = my_list
        del new_list[idx]
        return new_list
    else:
        return my_list
