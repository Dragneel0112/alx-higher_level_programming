#!/bin/bash
# Using curl to request from a URL and respond with a message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
