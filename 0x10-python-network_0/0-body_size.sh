#!/bin/bash
# A script that just takes in an URL, sends a request and then displays its  body's size of the response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
