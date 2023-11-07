#!/usr/bin/python3
"""contains a function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args:
        n (integer): Integer that represents the height of the triangle
    Return: list of list"""
    if n <= 0:
        return []
    tri = []
    for i in range(n):
        rw = []
        for j in range(i + 1):
            if j == 0 or j == i:
                rw.append(1)
            else:
                rw.append(tri[i - 1][j - 1] + tri[i - 1][j])
        tri.append(rw)
    return (tri)
