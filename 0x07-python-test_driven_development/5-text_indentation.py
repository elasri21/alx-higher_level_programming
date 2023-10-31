#!/usr/bin/python3
"""
5-text_indentation.py
"""


def text_indentation(text):
    """Prints extra lines after ., ? and :
    Args:
       text: text to work with"""

    if text is None:
        raise TypeError("text must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for dm in ".?:":
        text = (dm + "\n\n").join(
                [line.strip(" ") for line in text.split(dm)])
    print(text, end="")


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.tx")
