#!/bin/bash
# This script sends a POST request to the URL passed as argument with specified parameters and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
