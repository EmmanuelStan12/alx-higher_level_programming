#!/usr/bin/env bash
git add "$1"
git commit -m "$2"
echo "Committed $2 by $(date)";
