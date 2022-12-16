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
    try:
        with urllib.request.urlopen(url) as response:
            result = response.read().decode('utf-8')
            print(result)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    url = sys.argv[1]
    fetch(url)
