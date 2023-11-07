#!/usr/bin/python3
"""Contains a function that appends content
to a file"""


def append_write(filename="", text=""):
    """create a file if it does not exist and
    append content to its end
    Args:
        filename: the file name
        text: the text to append
    Return: number of character that are been appended"""
    with open(filename, "a") as f_name:
        return (f_name.write(text))
