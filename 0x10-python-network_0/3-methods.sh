#!/bin/bash
# Takes a url and displays the output
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
