#!/usr/bin/python3
"""Contains a script that fetches data from a url"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        data_utf = data.decode('utf-8')
        print("Body response:")
        print("\ttype: {}".format(type(data)))
        print("\tcontent: {}".format(data))
        print("\tutf8 content: {}".format(data_utf))
