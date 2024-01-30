#!/usr/bin/node

const request = require('request');

const urll = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(urll, function (error, response, body) {
  if (!error) {
    const chtrs = JSON.parse(body).characters;
    printCharacters(chtrs, 0);
  }
});

function printCharacters (characters, indx) {
  request(characters[indx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (indx + 1 < characters.length) {
        printCharacters(characters, indx + 1);
      }
    }
  });
}
