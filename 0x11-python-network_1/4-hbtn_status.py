#!/usr/bin/python3
"""
This module fetches the status from a given URL using the requests package.
"""

import requests


def fetch_status():
    """
    Fetches the status from a URL and displays the body response.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("    - type: {}".format(type(response.text)))
    print("    - content: {}".format(response.text))


if __name__ == "__main__":

    fetch_status()
