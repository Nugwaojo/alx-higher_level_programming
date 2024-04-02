#!/usr/bin/python3
"""
This module sends a POST request to http://0.0.0.0:5000/search_user with
a letter as a parameter and displays the response.
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user
    with a letter as a parameter and displays the response.
    """
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    search_user(letter)
