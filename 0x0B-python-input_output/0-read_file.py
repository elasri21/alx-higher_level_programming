#!/usr/bin/python3
"""contains a function that reads a file"""

def read_file(filename=""):
    """reads a file
    Args:
        filename: the file name"""
    with open(filename, "r") as f_name:
        file_content = f_name.read()
        print(file_content, end="")
