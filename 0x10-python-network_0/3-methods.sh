#!/bin/bash
# This script sends a request to the URL passed as argument and displays all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | awk -F ': ' '{print $2}'
