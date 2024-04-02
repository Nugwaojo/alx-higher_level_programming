#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file in the body and displays the response body

# Check if filename is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Check if file exists
if [ ! -f "$2" ]; then
    echo "File $2 not found"
    exit 1
fi

# Check if file is valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send JSON POST request and display response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
