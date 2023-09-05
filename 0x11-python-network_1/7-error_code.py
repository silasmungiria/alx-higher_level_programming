#!/usr/bin/python3
"""
This Python script performs the following tasks:
- Accepts a URL as a command-line argument.
- Sends an HTTP GET request to the specified URL.
- Displays the body of the response if the request is successful.
- If the request results in an HTTP error (status code 400 or higher),
  it prints the error code.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
