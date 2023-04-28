#!/bin/bash
# Using curl to send GET request and diplay header response from server
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id: 98"
