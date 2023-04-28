#!/bin/bash
# Using curl to display all methods the server will ALLOW
curl -sI "$1" | grep "ALLOW" | cut -d " " -f2-
