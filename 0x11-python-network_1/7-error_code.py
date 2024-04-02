#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the body of response,
handling HTTP status codes greater than or equal to 400.
"""

import requests
import sys


def display_response_body(url):
    """
    Sends a request to the URL and displays the body of the response.
    If the HTTP status code is > or = to 400, prints an error message.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    display_response_body(url)
