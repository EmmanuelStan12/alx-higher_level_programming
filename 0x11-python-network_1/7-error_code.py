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
    response = requests.get(url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)


if __name__ == '__main__':
    url = sys.argv[1]
    fetch(url)
