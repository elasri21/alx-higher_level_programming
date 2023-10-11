#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        if len(matrix) == 0:
            return (matrix)
        new_matrix = []
        for l in matrix:
            ul = []
            for i in l:
                ul.append(i**2)
            new_matrix.append(ul)
        return (new_matrix)
