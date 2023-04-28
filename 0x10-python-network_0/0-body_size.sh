#!/bin/bash
# Curls url and displays length of body
curl -sI GET "$1" | grep "Content-Length" | cut -d " " -f2
