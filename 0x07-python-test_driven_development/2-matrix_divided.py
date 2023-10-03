#!/usr/bin/python3
"""
This is the "2-matrix_divided.py" module. 
supplying matrix_divided function. Example,

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> matrix_divided(matrix,3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divides numbers of matrix by div and return the new matrix

    Args:
    matrix : list[list[int]]
    div: int|float

    """
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(num / div, 2) for num in row] for row in matrix]
    return new
