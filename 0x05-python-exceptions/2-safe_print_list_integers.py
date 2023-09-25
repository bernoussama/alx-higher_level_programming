#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            try:
                print("{:d}".format(int(my_list[i])))
                printed += 1
            except ValueError:
                pass
            except TypeError:
                pass

        except IndexError:
            return printed
    return printed