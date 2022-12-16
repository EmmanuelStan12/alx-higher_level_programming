#!/usr/bin/python3
"""
This file takes in url as input and gets a header value
"""
import requests
import sys


def post_email(url, email):
    """
    Posts data to a url
    """
    values = {'email': email}
    return requests.post(url, data=values)


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    result = post_email(url, email)
    print(result.text)
