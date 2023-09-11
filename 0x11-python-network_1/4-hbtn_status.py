#!/usr/bin/python3
"""
- Sends an HTTP GET request to the URL.
- Uses the 'requests' library for making the request.
- Prints information about the response received.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
