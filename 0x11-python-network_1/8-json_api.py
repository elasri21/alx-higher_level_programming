#!/usr/bin/python3
"""contains a script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys


def main(args):
    """to be called
    Args:
        args: command line arguments"""
    url = 'http://0.0.0.0:5000/search_user'
    q = ''
    if len(args) >= 2:
        q = args[1]
    data = {'q': q}
    res = requests.post(url, data=data)
    try:
        result = res.json()
        if bool(result) is False:
            print("No result")
        else:
            print("[{}] {}".format(result['id'], result['name']))
    except AttributeError:
        print('Not a valid JSON')


if __name__ == "__main__":
    main(sys.argv)
