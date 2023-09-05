#!/usr/bin/python3
def multiple(i, n):
    return True if i % n == 0 else False


def printnum(num):
    special = {3: "Fizz", 5: "Buzz"}
    # special[2] = "Deez"
    to_print = []
    for n, value in special.items():
        if multiple(num, n):
            to_print.append(value)

    to_print = "".join(s for s in to_print)
    print("{}".format(to_print if len(to_print) > 0 else num), end=" ")


def fizzbuzz():
    for i in range(1, 101):
        printnum(i)
