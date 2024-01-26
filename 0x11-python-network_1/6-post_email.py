#!/usr/bin/python3
"""Contains a script that takes in a URL and an email address, sends a
POST request to the passed URL with the email as a parameter, and finally
displays the body of the response."""
import requests
import sys


def main():
    """function tobe called"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    res = requests.post(url, data=data)
    text = res.text
    print(text)


if __name__ == "__main__":
    main()
