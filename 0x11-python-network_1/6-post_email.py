#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email as a parameter.
"""

import requests
import sys


def post_email(url, email):
    """
    Sends a POST request to the URL with the email as a parameter.
    """
    data = {'email': email}
    response = requests.post(url, data=data)
    print("Your email is:", email)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
