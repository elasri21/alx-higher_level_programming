#!/usr/bin/python3
"""contains the Student class"""


class Student:
    """This is a class student"""
    def __init__(self, first_name, last_name, age):
        """initializes an instance from Student
        Args:
            first_name: the persons first name
            last_name: the person's last name
            age: the person's age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        Args:
            attrs: list of strings
        Return: a dictionary in json representation"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__

        new_dict = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                new_dict[k] = v
        return (new_dict)
