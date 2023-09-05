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
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Create an HTTP request object for the provided URL
    request = urllib.request.Request(url)

    # Send the HTTP request and open the response
    with urllib.request.urlopen(request) as response:
        # Extract and print the 'X-Request-Id' from the response header
        x_request_id = dict(response.headers).get("X-Request-Id")
        print(f"X-Request-Id: {x_request_id}")
