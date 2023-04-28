#!/bin/bash
# Sends a request to a URL and displays the status code
curl -sw "%{http_code}" -o /dev/null "$1"
