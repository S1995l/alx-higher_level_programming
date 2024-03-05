#!/usr/bin/python3

"""
This script takes a URL as input, sends a request , and   displays the value .
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(request_id)
