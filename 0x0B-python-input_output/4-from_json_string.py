#!/usr/bin/python3
"""contais a function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """takes a string and return an object
    (Python data structure) represented by a JSON string
    Args:
        my_str: the string to encode with json
    Return: an object"""
    return (json.loads(my_str))
