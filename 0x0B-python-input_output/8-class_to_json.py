#!/usr/bin/python3
"""contains a  function that returns the dictionary description"""


def class_to_json(obj):
    """ returns the dictionary description
    Args:
        obj: the object
    Return: a dictionary"""
    return obj.__dict__
