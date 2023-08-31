#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL,
# and displays the size of the body of the response in bytes.

# Send a GET request to the provided URL and pipe the response body
# to "wc" command to count the bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

