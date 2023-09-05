#!/usr/bin/python3
for i in range(26):
    a = ord("a")
    if (a + i) == ord("e") or (a + i) == ord("q"):
        continue
    print(f"{chr(a+i)}", end="")
