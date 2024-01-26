#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge."""
import requests
import sys


def fetch_commits(repo, owner):
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    res = requests.get(url)    
    if res.status_code == 200:
        commits = res.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print("{}: {}".format(sha, author))


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    fetch_commits(repo, owner)
