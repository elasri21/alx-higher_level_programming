#!/usr/bin/python3
"""Module contains BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """calucates the area of the shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer
        Args:
            name: shape name
            value: an intege"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
