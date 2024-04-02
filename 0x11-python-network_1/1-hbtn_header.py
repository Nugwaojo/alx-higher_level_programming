#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def display_x_request_id(url):
    """
    Sends a request to the URL and displays the X-Request-Id value variable.
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    url = sys.argv[1]
    display_x_request_id(url)
