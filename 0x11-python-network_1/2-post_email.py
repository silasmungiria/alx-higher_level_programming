#!/usr/bin/python3
"""
A Python script that:
- Accepts a URL and an email as command-line arguments.
- Sends a POST request to the specified URL with the provided email as data.
- Displays the body of the response received from the URL.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Extract the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Create an HTTP POST request with the provided data
    request = urllib.request.Request(url, data)

    # Send the request and capture the response
    with urllib.request.urlopen(request) as response:
        # Display the body of the response as UTF-8 decoded content
        print(response.read().decode("utf-8"))
