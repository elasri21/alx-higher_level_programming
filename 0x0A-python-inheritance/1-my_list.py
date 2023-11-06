#!/usr/bin/python3
"""Declare a class that inherits from list object"""


class MyList(list):
    """Inherits from list object
    Args:
        list: the list object"""

    def print_sorted(self):
        """uses the copy and sort methods from list object
        and print a sorted list
        Return: nothing"""

        print(sorted(list(self)))
