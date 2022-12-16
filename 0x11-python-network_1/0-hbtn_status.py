#!/usr/bin/python3
"""
This file contains a function that does network operations
"""
import urllib.request


def fetch(url):
    """
    This fetches information from the url
    """
    with urllib.request.urlopen(url) as response:
        result = response.read()
    return result


if __name__ == '__main__':
    response = fetch('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode('utf-8')))
