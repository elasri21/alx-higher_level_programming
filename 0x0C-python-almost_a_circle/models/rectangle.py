#!/usr/bin/python3
"""Contains Rectangle class that inherits from Base class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Intialize an instance from the Rectangle class
        Args:
            width: rectangle width
            height: rectangle height
            x: Top left corner
            y: top left corner
            id: instance identifier"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set and get the width of the triangle"""
        return self.__width

    @width.setter
    def width(self, val):
        """set the width of the triangle
        Args:
            val: the value to assign to width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """set and get the height of the triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the triangle
        Args:
            value: the value to assign to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set and get the x corner of the triangle"""
        return self.__x

    @x.setter
    def x(self, xval):
        """set the x corner of the triangle
        Args:
            xval: the value to assign to x"""
        if type(xval) is not int:
            raise TypeError("x must be an integer")
        if xval < 0:
            raise ValueError("x must be >= 0")
        self.__x = xval

    @property
    def y(self):
        """set and get the y corner of the triangle"""
        return self.__y

    @y.setter
    def y(self, yval):
        """set the y corner of the triangle
        Args:
            yval: the value to assign to y"""
        if type(yval) is not int:
            raise TypeError("y must be an integer")
        if yval < 0:
            raise ValueError("y must be >= 0")
        self.__y = yval

    def area(self):
        """calculates the reclangle area
        Return: area"""
        return (self.__width * self.__height)

    def display(self):
        """displays a rectangle using #"""
        for s in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width + self.__x):
                if j < self.__x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        """modify the behavior of the dunder function str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Updates the order of the instance properties
        Args:
            args: tuple contains all the arguments
            kwargs: dictinary like of key/value pairs"""
        length = len(args)
        if length > 0:
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.height = args[2]
            if length >= 4:
                self.x = args[3]
            if length >= 5:
                self.y = args[4]
        else:
            props = list(kwargs.keys())
            if "id" in props:
                self.id = kwargs["id"]
            if "width" in props:
                self.width = kwargs["width"]
            if "height" in props:
                self.height = kwargs["height"]
            if "x" in props:
                self.x = kwargs["x"]
            if "y" in props:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """get a dictionary from the instance attributes
        Return: a dictinary"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
