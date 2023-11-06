#!/usr/bin/python3
"""Contains a class that inherits from int"""


class MyInt(int):
    """A class that inherits from int"""

    def __eq__(self, other):
        """dreverse the useul behavior
        Args:
            other: another class
        Return: Fasle if other equal to self. True otherwise"""
        return int(self) != other

    def __ne__(self, other):
        """dreverse the useul behavior
        Args:
            other: another class to compare with
        Return: True if other equal to self. True otherwise"""
        return int(self) == other
