#!/usr/bin/python3
"""
The say_my_name Module
"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    Args:
        first_name: is the first name
        last_name: is the second name"""
    if first_name is None:
        raise TypeError("Missing 1 required position argument 'first_name'")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
