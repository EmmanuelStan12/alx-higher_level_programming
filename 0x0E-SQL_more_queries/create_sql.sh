#!/usr/bin/env bash
touch "$1.sql"
echo "-- $2" > "$1.sql";
vim "$1.sql";
