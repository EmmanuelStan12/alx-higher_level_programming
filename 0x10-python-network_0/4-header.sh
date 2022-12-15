#!/usr/bin/bash
# Takes a url and displays the output
curl -sL -X GET "$1" \
	-H "X-School-User-id: 98"
