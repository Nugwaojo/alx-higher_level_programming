#!/usr/bin/python3
"""
This module uses Basic Authentication with a personal access token to access
GitHub API and displays the user id.
"""

import requests
import sys


def get_user_id(username, password):
    """
    Uses Basic Authentication with a personal access token to access
    GitHub API and displays the user id.
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        return response.json()['id']
    else:
        return None


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    user_id = get_user_id(username, password)
    print(user_id)
