#!/usr/bin/python3
"""Contains a function that checks
if an object is instance of a class"""


def is_same_class(obj, a_class):
    """check if an object is instance from a class
    Args:
        obj: object to check
        a_class: class to check
    Return: True if so. False otherwise"""

if dir(obj) == dir(a_class):
        return (True)
    else:
        return (False)
