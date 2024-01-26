#!/usr/bin/python3
"""Contains a script that fetches data from a url"""
import urllib.request

def main():
    """The main function to be called"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        data = res.read()
        data_utf = data.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data_utf))


if __name__ == "__main__":
    main()
