#!/bin/bash
# This gets the length of a response
curl -sI "$1" | grep "Content-Length" | cut -d" " -f2 | xargs
