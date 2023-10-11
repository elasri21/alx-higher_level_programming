#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        if len(matrix) == 0:
            return (matrix)
        new_matrix = matrix.copy()
        for l in matrix:
            l = list(map(lambda i: i**2, l))
        return (new_matrix)
