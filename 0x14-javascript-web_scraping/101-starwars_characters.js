#!/usr/bin/node

const requst = require('request');

const urll = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

requst(urll, function (error, response, body) {
  if (!error) {
    const chtrs = JSON.parse(body).characters;
    printCharacters(chtrs, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
