#!/usr/bin/python3
"""
This Python script performs the following tasks:
- Accepts your GitHub credentials (username and password) as command-line,
  arguments.
- Uses the GitHub API to make an authenticated request to fetch your user,
  information.
- Retrieves and displays your GitHub user ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)

    r = requests.get("https://api.github.com/user", auth=auth)

    print(r.json().get("id"))
