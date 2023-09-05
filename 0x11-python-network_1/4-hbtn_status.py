#!/usr/bin/python3
"""
A Python script that performs the following tasks:
- Sends an HTTP GET request to the URL https://intranet.hbtn.io/status.
- Uses the 'requests' library for making the request.
- Prints information about the response received.

Note: This script is intended to fetch and display the content of the given URL.
"""

import requests

if __name__ == "__main__":
    # Send an HTTP GET request to the specified URL
    r = requests.get("https://intranet.hbtn.io/status")

    # Print information about the response
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
