#!/usr/bin/node

const requst = require('request');

const urrl = process.argv[2];

requst(urrl, function (errr, response, body) {
  if (errr) {
    console.log(errr);
  } else if (response.statusCode === 200) {
    const complleted = {};

    const taskss = JSON.parse(body);
    for (const x in taskss) {
      const tassk = taskss[x];
      if (tassk.complleted === true) {
        if (complleted[tassk.userId] === undefined) {
          complleted[tassk.userId] = 1;
        } else {
          complleted[tassk.userId]++;
        }
      }
    }
    console.log(complleted);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
