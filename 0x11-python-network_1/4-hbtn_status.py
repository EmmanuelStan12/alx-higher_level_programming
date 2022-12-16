#!/usr/bin/python3
"""
This file contains a function that does network operations
"""
import requests


def fetch(url):
    """
    This fetches information from the url
    """
    response = requests.get(url)
    return response


if __name__ == '__main__':
    response = fetch('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
