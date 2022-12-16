#!/usr/bin/python3
"""
This file takes in url as input and gets a header value
"""
import requests
import sys


def fetch(url):
    """
    Fetches data from a url
    """
    return requests.get(url).headers


if __name__ == '__main__':
    url = sys.argv[1]
    headers = fetch(url)
    print(headers['X-Request-Id'])
