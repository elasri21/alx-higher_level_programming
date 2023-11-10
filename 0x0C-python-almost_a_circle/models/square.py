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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """"modify the behavior of str dunder function"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
