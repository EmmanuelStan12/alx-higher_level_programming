#!/usr/bin/python3
"""
This file takes in url as input and gets a header value
"""
import urllib.request
import sys


def fetch(url):
    """
    Fetches data from a url
    """
    with urllib.request.urlopen(url) as response:
        result = response.getheaders()
    headers = {key: value for key, value in result}
    return headers


if __name__ == '__main__':
    url = sys.argv[1]
    headers = fetch(url)
    print(headers.get('X-Request-Id'))
