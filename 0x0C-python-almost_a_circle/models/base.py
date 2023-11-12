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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            cls: class
            list_objs: list of objects"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f_name:
            if not list_objs:
                json.dump(json.loads("[]"), f_name)
            else:
                json.dump(
                     json.loads(
                          cls.to_json_string(
                              [obj.to_dictionary() for obj in list_objs]
                          )
                     ),
                     f_name
                )

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string: json string"""
        if not json_string:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            cls: the class
            dictionary: dictionary containing properties of cls
        Return: an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances
        Args:
            cls: class
        Return:  returns a list of instances"""
        try:
            file_name = cls.__name__ + ".json"
            with open(file_name, "r") as f_name:
                content = f_name.read()
                ls = [list_o for list_o in cls.from_json_string(content)]
                return [cls.create(**{k: v for k, v in d.items()}) for d in ls]
        except FileNotFoundError:
            return []
