#!/usr/bin/python3
"""
This module retrieves the most recent 10 commits of repository from GitHub API
"""

import requests
import sys


def get_commits(repo_name, owner_name):
    """
    Retrieves the most recent 10 commits of a given repository from GitHub API
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Get the most recent 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo_name> <owner_name>")
        sys.exit(1)
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repo_name, owner_name)
