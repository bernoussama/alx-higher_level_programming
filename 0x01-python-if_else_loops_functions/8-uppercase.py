#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return True
    else:
        return False


def uppercase(str):
    offset = ord("A") - ord("a")
    for char in str:
        char = chr(ord(char) + offset) if islower(char) else char
        print("{}".format(char), end="")
    print()
