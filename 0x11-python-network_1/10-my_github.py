#!/usr/bin/python3
"""
This shows my Github
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))
