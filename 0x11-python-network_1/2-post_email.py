#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email as a parameter
"""

import urllib.parse
import urllib.request
import sys


def post_email(url, email):
    """
    Sends a POST request to the URL with the email as a parameter
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    print("Your email is:", email)
    post_email(url, email)
