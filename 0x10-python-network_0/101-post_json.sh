#!/bin/bash
# Sends a JSON POST request and  displays response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
