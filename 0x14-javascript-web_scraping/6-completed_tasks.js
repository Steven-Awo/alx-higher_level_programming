#!/usr/bin/node

const requst = require('request');

const urll = process.argv[2];

requst(urll, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const complteted = {};
    const tassks = JSON.parse(body);
    for (const x in tassks) {
      const taskk = tassks[x];
      if (taskk.complteted === true) {
        if (complteted[taskk.userId] === undefined) {
          complteted[taskk.userId] = 1;
        } else {
          complteted[taskk.userId]++;
        }
      }
    }
    console.log(complteted);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
