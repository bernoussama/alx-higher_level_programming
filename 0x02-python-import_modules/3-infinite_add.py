#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, stderr

    argc = len(argv) - 1
    if argc == 0:
        print(0)
    else:
        addition = 0
        for i in range(1, argc + 1):
            try:
                addition += int(argv[i])
            except ValueError as e:
                stderr.write(f"{argv[i]} is not a number.\n{e}")
                exit(1)
        print(addition)
