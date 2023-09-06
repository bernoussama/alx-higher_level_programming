#!/usr/bin/python3
for i in range(26):
    z = "z" if not i % 2 else "Z"
    print("{}".format(chr(ord(z) - i)), end="")
