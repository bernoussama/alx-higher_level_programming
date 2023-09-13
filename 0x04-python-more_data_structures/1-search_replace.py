#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def rep(x):
        return replace if x == search else x

    new_list = list(map(rep, my_list))
    return new_list
