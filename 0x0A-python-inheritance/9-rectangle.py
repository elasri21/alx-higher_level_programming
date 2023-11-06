#!/usr/bin/python3
"""module contains Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""
    def __init__(self, width, height):
        """initializes a rectangle
        Args:
            width: rectangle width
            height: rectangle height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates the rectangle area"""
        return (self.__width * self.__height)

    def __str__(self):
        """modify the dunder function str"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
