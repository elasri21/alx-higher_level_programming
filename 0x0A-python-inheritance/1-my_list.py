#!/usr/bin/python3
"""Declare a class that inherits from list object"""


class MyList(list):
    """Inherits from list object"""
    pass

    def print_sorted(self):
        """uses sorted method to print a list"""
        print(sorted(list(self)))


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/1-my_list.txt")
