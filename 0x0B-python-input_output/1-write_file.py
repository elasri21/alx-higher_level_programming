#!/usr/bin/python3


def write_file(filename="", text=""):
    """writes to a file and creates it if it is not exist
    Args:
        filename: the file name
        text: text to write to the file
    Return: the number of character that are been witten"""
    with open(filename, "w") as file:
        return (file.write(text))
