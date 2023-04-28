#!/bin/bash
# Using curl to display all methods the server will ALLOW
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
