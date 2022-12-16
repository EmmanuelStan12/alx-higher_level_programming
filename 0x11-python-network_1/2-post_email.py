#!/usr/bin/python3
"""
This file takes in url as input and gets a header value
"""
import urllib.request
import sys


def post_email(url, email):
    """
    Posts data to a url
    """
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        result = response.read()
    return result


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    result = post_email(url, email).decode('utf-8')
    print(result)
