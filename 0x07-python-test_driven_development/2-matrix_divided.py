#!/usr/bin/python3
"""Module for matrix_divided"""


def matrix_divided(matrix, div):
    """divides all matrix element by div
       Args:
           matrix: the matrix
           div: the number to divide by

       Raies:
           TypeError: if matrix element are not float or integer
           ZeroDivisionError: if div is zero

       Return: New matrix
    """
    if matrix is None or div is None:
        raise TypeError("matrix_divided() missing 2 required positional " +
                        "arguments: 'matrix' and 'div'")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for list_ch in matrix:
        if not isinstance(list_ch, list) or len(list_ch) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(list_ch) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for list_ch in matrix:
        for item in list_ch:
            if type(item) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            if item + 1 == item:
                raise TypeError("Overflow")
    new_list = []
    for list_ch in matrix:
        new_ch = []
        for n in list_ch:
            res = round(n / div, 2)
            new_ch.append(res)
        new_list.append(new_ch)
    return (new_list)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
