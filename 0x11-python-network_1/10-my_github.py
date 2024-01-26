#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys


def main():
    """to be called"""
    username = sys.argv[1]
    pass_tocken = sys.argv[2]
    url = 'https://api.github.com/user'
    authentication = (username, pass_tocken)
    res = requests.get(url, auth=authentication)
    if res.status_code == 200:
        user_data = res.json()
        print(user_data['id'])
    else:
        print('None')


if __name__ == "__main__":
    main()
