#!/usr/bin/python3
"""
my list module
"""


class MyList(list):
    """
    MyList inherits from list
    """

    def print_sorted(self):
        print(sorted(self))
