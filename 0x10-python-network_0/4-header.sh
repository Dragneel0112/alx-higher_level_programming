#!/bin/bash
# Using curl to send GET request and diplay header response from server
curl -sX GET -H "X-School-User-Id: 98" "$1"
