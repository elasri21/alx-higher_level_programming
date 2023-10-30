#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    """integer represents the number of instances"""

    print_symbol = '#'
    """String character"""

    def __init__(self, width=0, height=0):
        """initialize a new instance
        Args:
            width (integer): the width
            height (integer): the height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the with property"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width property
        Args:
            width (integer): the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height property"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height property
        Args:
            height (integer): the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """calculates and return the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates and return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            row = []
            for j in range(self.__width):
                row.append(self.print_symbol)
            rect.append("".join(row))
        return ("\n".join(rect))

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """inform that an instance was deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


