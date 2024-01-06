#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
import sys
from requests.models import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"

    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    res = r.json()
    print(res.get("id"))
