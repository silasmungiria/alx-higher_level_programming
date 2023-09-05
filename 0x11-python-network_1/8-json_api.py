#!/usr/bin/python3
"""
This Python script performs the following tasks:
- Accepts a single letter as a command-line argument or defaults to an empty,
  string if no argument is provided.
- Sends an HTTP POST request to http://0.0.0.0:5000/search_user with the,
  letter as a parameter.
- Handles the response, which is expected to be in JSON format.
- Prints the user's ID and name if a result is found in the response.
- If no result is found, it prints "No result."
- If the response is not valid JSON, it prints "Not a valid JSON."
"""

import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        response = r.json()

        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
