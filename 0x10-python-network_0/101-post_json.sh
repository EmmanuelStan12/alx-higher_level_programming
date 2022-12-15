#!/bin/bash
# This sends a post request to a URL
curl -sX "POST" -H "Content-Type: application/json" -d "@$2" "$1"
