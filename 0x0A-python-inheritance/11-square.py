#!/usr/bin/python3
"""module contains square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""
    def __init__(self, size):
        """initializes a square
        Args:
            size: square side"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the square area"""
        return (self.__size * self.__size)

    def __str__(self):
        """print a readable format"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
