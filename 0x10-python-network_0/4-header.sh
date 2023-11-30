#!/bin/bash
# This script sends a GET request to a URL along with a header variable
curl -s "$1" -H "X-School-User-Id: 98"
