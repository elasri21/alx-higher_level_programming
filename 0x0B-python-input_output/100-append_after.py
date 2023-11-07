#!/usr/bin/python3
"""contains  a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string
    Args:
        filename: the file name
        search_string: the string pattern to look for
        new_string: new string to insert"""
    with open(filename, "r", encoding='utf-8') as f_name:
        list_lines = []
        while True:
            line = f_name.readline()
            if line == "":
                break
            list_lines.append(line)
            if search_string in line:
                list_lines.append(new_string + "\n")
    with open(filename, "w", encoding='utf-8') as f_name:
        for new_line in list_line:
            f_name.writelines(new_line)
