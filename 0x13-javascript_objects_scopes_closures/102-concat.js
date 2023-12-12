#!/usr/bin/node

const fls = require('fs');

const frstlArg = fls.readFileSync(process.argv[2]).toString();

const secndlArg = fls.readFileSync(process.argv[3]).toString();

fls.writeFileSync(process.argv[4], frstlArg + secndlArg);
