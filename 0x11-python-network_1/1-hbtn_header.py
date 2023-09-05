#!/usr/bin/python3
"""
A Python script that performs the following tasks:
- Takes a URL as a command-line argument.
- Sends an HTTP request to the specified URL.
- Extracts and displays the value of the 'X-Request-Id' variable from,
  the response header.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
