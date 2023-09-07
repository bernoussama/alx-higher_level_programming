#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    if argc > 0:
        print(f"{argc} arguments:")
    else:
        print("0 arguments.")

    for idx, arg in enumerate(argv):
        if idx != 0:
            print(f"{idx}: {arg}")
