#!/usr/bin/python3
"""Contains a function that returnsmethods and properties
of an object"""


def lookup(obj):
    """get all properties and methods of an object
    Args:
        obj: the object
    Return: a list of all methods and properties"""

    return (list(dir(obj)))
