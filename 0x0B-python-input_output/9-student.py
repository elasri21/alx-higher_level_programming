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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
