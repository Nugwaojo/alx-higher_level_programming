#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the value
of the X-Request-Id variable found in the response header.
"""

import requests
import sys


def display_x_request_id(url):
    """
    Sends a request to the URL and displays the X-Request-Id variable value.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    display_x_request_id(url)
