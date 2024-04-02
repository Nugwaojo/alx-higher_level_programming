#!/usr/bin/python3
"""
This module fetches the status from a given URL using urllib package.
"""

import urllib.request


def fetch_status():

    """
    Fetches the status from a URL and displays the body response.
    """
    url = 'https://intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":

    fetch_status()
