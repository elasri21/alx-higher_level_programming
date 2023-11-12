#!/usr/bin/python3
"""Contains the Base class"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new instance from the class
        Args:
            id: instance identifier"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string representation
        Args:
            list_dictionaries: list of dictionaries
        Return: json representation of a string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
