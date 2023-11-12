#!/usr/bin/python3
"""contains square class that inherits from reclangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from Rectanglr
    Args:
        Rectangle: Class to inherit from"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialises an instance from Square
        Args:
            size: the size of the squae
            x: left
            y: top
            id: identifier"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get and set the size property"""
        return self.width

    @size.setter
    def size(self, val):
        """set the size of the rectangle
        Args:
            val: the value to assign to width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """using args and kwargs to pass parameters
        Args:
            args: tuple contains arguments
            kwargs: dictionary contains args"""
        length = len(args)
        if length > 0:
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.size = args[1]
            if length >= 3:
                self.x = args[2]
            if length >= 4:
                self.y = args[3]
        else:
            props = list(kwargs.keys())
            if "id" in props:
                self.id = kwargs["id"]
            if "size" in props:
                self.width = kwargs["size"]
            if "x" in props:
                self.x = kwargs["x"]
            if "y" in props:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """get a dictionary from the instance attributes
        Return: a dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """"modify the behavior of str dunder function"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
