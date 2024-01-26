#!/usr/bin/python3
"""Contains a script that fetches data from a url"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    data_utf = data.decode('utf-8')
    print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(data), data, data_utf))
