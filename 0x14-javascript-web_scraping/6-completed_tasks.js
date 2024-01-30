#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const complleted = {};
    const tasks = JSON.parse(body);
    for (const x in tasks) {
      const task = tasks[x];
      if (task.completed === true) {
        if (complleted[task.userId] === undefined) {
          complleted[task.userId] = 1;
        } else {
          complleted[task.userId]++;
        }
      }
    }
    console.log(complleted);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
