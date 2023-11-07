#!/usr/bin/python3


def read_file(filename=""):
    """reads a file
    Args:
        filename: the file name"""
    with open(filename, "r") as file:
        file_content = file.read()
        print(file_content, end="")
