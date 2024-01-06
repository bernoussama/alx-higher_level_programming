#!/usr/bin/python3
"""

"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    res = r.json()
    # print(res)
    # print(res.get("id"))
    for commit in res:
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author_name}")
