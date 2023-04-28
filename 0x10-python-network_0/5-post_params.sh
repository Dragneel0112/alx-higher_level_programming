#!/bin/bash
# Using curl to send Post request and display response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
