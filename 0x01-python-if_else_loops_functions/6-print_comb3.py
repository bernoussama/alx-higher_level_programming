#!/usr/bin/python3
k = 1
for i in range(10):
    for j in range(k, 10):
        if i == 8 and j == 9:
            print("{:d}{:d},".format(i, j))
            break
        if i != j:
            print("{:d}{:d},".format(i, j), end=" ")

    k += 1
