# Project Title: 0x11. Python - Network #1

## Description
This project is part of the Holberton School curriculum and aims to teach you how to work with network requests and APIs using Python. You will learn how to fetch internet resources, handle HTTP requests, and interact with external services. The tasks in this project cover a range of topics related to network programming in Python.

## Project Structure
The project consists of multiple Python scripts, each addressing a specific task related to network programming. Here's a brief overview of each task and its corresponding script:

### Task 0: What's my status? #0
- **Script:** 0-hbtn_status.py
- **Description:** Fetches the https://alx-intranet.hbtn.io/status URL using the urllib package and displays information about the response body, including its type and content.

### Task 1: Response header value #0
- **Script:** 1-hbtn_header.py
- **Description:** Takes a URL as input, sends an HTTP request to the URL using urllib, and displays the value of the X-Request-Id variable found in the response header.

### Task 2: POST an email #0
- **Script:** 2-post_email.py
- **Description:** Takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response (decoded in utf-8).

### Task 3: Error code #0
- **Script:** 3-error_code.py
- **Description:** Takes a URL as input, sends an HTTP request to the URL using urllib, and displays the body of the response (decoded in utf-8). Handles urllib.error.HTTPError exceptions and prints the error code if it occurs.

### Task 4: What's my status? #1
- **Script:** 4-hbtn_status.py
- **Description:** Fetches the https://alx-intranet.hbtn.io/status URL using the requests package and displays information about the response body, including its type and content.

### Task 5: Response header value #1
- **Script:** 5-hbtn_header.py
- **Description:** Takes a URL as input, sends an HTTP request to the URL using requests, and displays the value of the X-Request-Id variable in the response header.

### Task 6: POST an email #1
- **Script:** 6-post_email.py
- **Description:** Takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter using requests, and displays the body of the response.

### Task 7: Error code #1
- **Script:** 7-error_code.py
- **Description:** Takes a URL as input, sends an HTTP request to the URL using requests, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints an error message with the status code.

### Task 8: Search API
- **Script:** 8-json_api.py
- **Description:** Takes a letter as input and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter. It then processes the JSON response and displays the user's id and name if found, or appropriate error messages.

### Task 9: My GitHub!
- **Script:** 10-my_github.py
- **Description:** Takes your GitHub username and a personal access token as input and uses the GitHub API with Basic Authentication to display your GitHub user ID.

### Task 10: Time for an interview! (Advanced)
- **Script:** 100-github_commits.py
- **Description:** Takes two arguments, a repository name and an owner name, and uses the GitHub API to list the 10 most recent commits of the specified repository. It prints each commit's SHA and author name.

## Usage
To run any of the scripts, use the following format:
```
./script_name.py [additional_arguments]
```

Make sure you have the required packages installed and that your Python environment meets the specified requirements for each task.

## Author
- **Author:** Guillaume, CTO at Holberton School & Silas

## License
This project is licensed under the terms of the MIT License.
