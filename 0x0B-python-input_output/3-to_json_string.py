#!/usr/bin/python3
"""Contains a function that returns JSON representation
of an object"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object
    Args:
        my_obj: the object to handle
    Return: the JSON representation"""
    return (json.dumps(my_obj))
