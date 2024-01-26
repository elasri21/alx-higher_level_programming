#!/usr/bin/python3
"""Contains a script that takes in a URL, sends a request
to the URL and displays the body of the response."""
import requests
import sys


def main():
    """function to be called"""
    url = sys.argv[1]
    res = requests.get(url)
    text = res.text
    print(text)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))


if __name__ == "__main__":
    main()
