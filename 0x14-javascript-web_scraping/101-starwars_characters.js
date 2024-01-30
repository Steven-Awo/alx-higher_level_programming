#!/usr/bin/node

const reqt = require('request');

const urll = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

reqt(urll, function (error, response, body) {
  if (!error) {
    const chtrs = JSON.parse(body).chtrs;
    printCharacters(chtrs, 0);
  }
});

function printCharacters (chtrs, indx) {
  reqt(chtrs[indx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (indx + 1 < chtrs.length) {
        printCharacters(chtrs, indx + 1);
      }
    }
  });
}
