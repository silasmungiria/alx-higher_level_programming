#!/usr/bin/python3
"""
A Python script that retrieves and displays the 'X-Request-Id' header variable
from an HTTP GET request to a specified URL.
 - Get the URL from the command-line argument
 - Send an HTTP GET request to the specified URL
 - Retrieve and print the 'X-Request-Id' header value
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
