#!/usr/bin/python3
islower = __import__("7-islower").islower


def uppercase(str):
    offset = ord("A") - ord("a")
    for char in str:
        print("{}".format(chr(ord(char) + offset) if islower(char) else char), end="")
    print()
