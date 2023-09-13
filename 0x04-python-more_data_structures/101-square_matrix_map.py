#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list()
    for row in matrix:
        new_matrix.append(list(map(lambda x: x**2, row)))
    return new_matrix
