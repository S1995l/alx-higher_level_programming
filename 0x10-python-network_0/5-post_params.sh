#!/bin/bash
# This script takes a URL as input, sends a POST request to the URL with specified variables in the request body, and displays the body of the response.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
