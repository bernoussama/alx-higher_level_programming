#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    param = ""
    if len(sys.argv) > 1:
        param = sys.argv[1]

    payload = {"q": param}

    r = requests.post(url, data=payload)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            id, name = res.get("id"), res.get("name")
            print(f"[{id}] {name}")

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
