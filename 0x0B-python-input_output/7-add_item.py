#!/usr/bin/python3

"""
add_item module
----------------
script that adds all arguments to a Python list, and then save them to a file

"""
import json
from sys import argv

if __name__ == "__main__":
    """
    add_item main function

    """

    filename = "add_item.json"

    # load file if exists
    loaded = None
    try:
        with open(filename, "r", encoding="utf-8") as f:
            loaded = json.load(f)
    except FileNotFoundError:
        pass

    # append to it or create it
    with open(filename, "w+", encoding="utf-8") as f:
        if loaded is not None:
            items = loaded
        else:
            items = []

        # update the list
        for idx, arg in enumerate(argv):
            if idx == 0:
                continue
            items.append(arg)

        # dumps the updated list to it
        json.dump(items, f)
