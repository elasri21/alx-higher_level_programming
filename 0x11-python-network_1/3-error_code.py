#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)"""
import urllib.request
import urllib.error
import urllib.parse
import sys


def main():
    """The main function to be called"""
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body_cont = res.read().decode('utf-8')
            print(body_cont)
    except urllib.error.HTTPError as err:
        print("Error code: ".format(err.code))


if __name__ == "__main__":
    main()
