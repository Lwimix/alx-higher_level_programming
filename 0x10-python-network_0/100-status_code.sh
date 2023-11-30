#!/bin/sh
# This script displays the status code for a requested page
curl -o /dev/null -sw "%{http_code}\n" -s "$1"
