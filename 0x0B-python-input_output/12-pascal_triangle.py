#!/usr/bin/python3
"""pascal_triangle module

"""


def pascal_triangle(n):
    """
    that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    output = []
    for i in range(n):
        if i == 0:
            output.append([1])
            continue
        else:
            row = []
            previous = [0] + output[i - 1] + [0]
            for j in range(i + 1):
                left = previous[j - 1 + 1]
                right = previous[j + 1]
                row.append(left + right)
            output.append(row)
    return output
