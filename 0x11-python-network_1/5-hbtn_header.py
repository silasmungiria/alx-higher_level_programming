#!/usr/bin/python3
"""
A Python script that retrieves and displays the 'X-Request-Id' header variable
from an HTTP GET request to a specified URL.
 - Get the URL from the command-line argument
 - Send an HTTP GET request to the specified URL
 - Retrieve and print the 'X-Request-Id' header value
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
