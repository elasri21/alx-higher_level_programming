#!/usr/bin/python3
"""contains a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename: the file"""
    with open(filename, "r") as f_name:
        content = f_name.read()
        return (json.loads(content))
