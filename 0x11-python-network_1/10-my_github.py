#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/users/{username}"

    r = requests.get(
        url, auth=requests.models.HTTPBasicAuth(
            username, password))
    print(r.json().get("id"))
