#!/usr/bin/python3
"""Contains a script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response."""
import urllib.request
import sys


def main():
    """the main functiomto be called"""
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers['X-Request-Id'])


if __name__ == "__main__":
    main()
