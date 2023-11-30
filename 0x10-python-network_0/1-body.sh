#!/bin/bash
# This script sends a GET request and only returns a
#+response with a 200 status code
grep "200 OK" | curl -sL "$1"
