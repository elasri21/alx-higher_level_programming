#!/usr/bin/python3
"""contains an empty a function that checks if
an object is inherited from a class"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args:
        obj: the object to check
        a_class: The class to check against
    Return: True if so. False otherwise"""

if type(obj) is a_class:
        return (False)
    elif isinstance(obj, a_class):
        return (True)
