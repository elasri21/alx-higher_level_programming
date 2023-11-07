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
    with open(filename, "r") as f_name:
        lines = f_name.readlines()
        list_lines = []
        for ln in lines:
            if ln.find(search_string) != -1:
                list_lines.append(ln)
                list_lines.append("\n".join(new_string))
            else:
                list_lines.append(ln)
    with open(filename, "w") as f_name:
        for new_line in list_line:
            f_name.write(new_line)
