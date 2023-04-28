#!/bin/bash
# Using curl to send GET request and diplay header response from server
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
