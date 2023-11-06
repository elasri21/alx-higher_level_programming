#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of a class
    or is an instance of a class that inherited the class
    Args:
        obj: the object to check
        a_class: the class to check against
    Return: True is so. False otherwise"""
    
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
