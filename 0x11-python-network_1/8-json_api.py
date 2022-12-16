#!/usr/bin/python3
"""
This sends a post request to a url
"""
import requests
import sys


def search(query, url):
    """
    The search function sends a post request
    """
    response = requests.post(url, data={'q': query})
    try:
        r_json = response.json()
        id, name = r_json.get('id'), r_json.get('name')
        if len(r_json) == 0 or not id or not name:
            return "No result"
        else:
            return "[{}] {}".format(id, name)
    except e:
        return "Not a valid JSON"


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    query = sys.argv[1] if len(sys.argv) == 2 else ""
    data = search(query, url)
    print(data)
