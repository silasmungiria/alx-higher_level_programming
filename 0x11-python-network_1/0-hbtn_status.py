#!/usr/bin/python3
"""
A Python script that demonstrates the following:
- Fetches data from the URL https://alx-intranet.hbtn.io/status.
- Utilizes the urllib package for HTTP requests.
"""

if __name__ == '__main__':
    import urllib.request

    # Send an HTTP GET request to the specified URL
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()

        # Print information about the response
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
