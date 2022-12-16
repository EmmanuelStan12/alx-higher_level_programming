#!/bin/bash
# This sends a post request to a URL
curl -sX "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
