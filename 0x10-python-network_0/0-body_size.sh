#!/bin/bash
# A script that just takes in an URL, sends a request and then displays its  body's size of the response
curl -sI "$1" | awk "Content-Length:/ {print $2}" | tr -d "\r\n "
