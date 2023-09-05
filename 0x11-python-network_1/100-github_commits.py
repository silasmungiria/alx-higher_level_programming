#!/usr/bin/python3
"""
This Python script lists the 10 most recent commits on a specified GitHub repository.
 - Construct the GitHub API URL for retrieving commits
 - Send an HTTP GET request to the GitHub API
 - Parse the JSON response into a list of commits
 - Print the 10 most recent commits
 - Handle the case where there are fewer than 10 commits
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])

    r = requests.get(url)

    commits = r.json()

    try:
        for i in range(10):
            commit = commits[i]
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
