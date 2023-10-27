#!/usr/bin/python3
"""
This module contains a function that returns
the result of summing two integers
and return it
"""


def add_integer(a, b=98):
    """
        Return the result of a + b
    """
    result = 0
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return (result)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
