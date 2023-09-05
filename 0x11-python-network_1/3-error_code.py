#!/usr/bin/python3
"""
A Python script that performs the following tasks:
- Accepts a URL as a command-line argument.
- Sends an HTTP request to the provided URL.
- Displays the body of the response, decoded using UTF-8.
- Handles and displays HTTP errors if encountered.
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        # Send an HTTP request to the URL specified in the command line
        with request.urlopen(sys.argv[1]) as res:
            # Display the decoded content of the response
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        # Handle and display the HTTP error code if encountered
        print('Error code:', er.code)
