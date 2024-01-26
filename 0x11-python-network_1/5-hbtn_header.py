#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header"""
import requests
import sys


def main():
    """function to be called"""
    url = sys.argv[1]
    res = requests.get(url)
    req_id = res.headers.get('X-Request-Id')
    print(req_id)


if __name__ == "__main__":
    main()
