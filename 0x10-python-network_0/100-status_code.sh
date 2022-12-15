#!/bin/bash
# This finds the http status code of a response
curl -sL -w '%{http_code}' -o /dev/null "$1"
