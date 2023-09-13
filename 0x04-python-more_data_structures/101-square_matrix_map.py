#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list(map(lambda row: list(map(lambda y: y**2, row)), matrix))
    return new_matrix
