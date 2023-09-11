#!/usr/bin/python3
def print_matrix_integer(matrix: list[list[int]] = [[]]):
    for row in matrix:
        print(*[str.format("{:d}", el) for el in row], sep=" ", end="\n")
