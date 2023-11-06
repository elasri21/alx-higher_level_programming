#!/usr/bin/python3
"""This Module contains function that adds an
attribute to an object is it is possible"""


def add_attribute(obj, att, val):
    """adds an attribute to an object is it is possible
    Args:
        obj: the object
        att: attribute to add
        val: attribute value"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
