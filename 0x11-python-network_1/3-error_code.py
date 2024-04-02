#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the body of response,
handling urllib.error.HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys


def error_code(url):
    """
    Sends a request to the URL and displays the body of the response,
    handling urllib.error.HTTPError exceptions.
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    url = sys.argv[1]
    error_code(url)
