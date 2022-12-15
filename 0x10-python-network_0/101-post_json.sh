#!/bin/bash
# This sends a post request to a URL
curl -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"
