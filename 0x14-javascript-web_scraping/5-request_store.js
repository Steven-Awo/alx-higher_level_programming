#!/usr/bin/node

const fss = require('fs');

const requst = require('request');

requst(process.argv[2]).pipe(fss.createWriteStream(process.argv[3]));
