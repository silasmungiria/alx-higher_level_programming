#!/usr/bin/python3
"""
A Python script that performs the following tasks:
- Sends an HTTP GET request to the URL https://intranet.hbtn.io/status.
- Uses the 'requests' library for making the request.
- Prints information about the response received.
"""

import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
