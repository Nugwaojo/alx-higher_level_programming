#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument
# with the contents of a file passed as the second argument in the body, using curl

if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

if [ ! -f "$2" ]; then
    echo "File $2 not found"
    exit 1
fi

if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
