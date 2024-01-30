#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const resultts = JSON.parse(body).resultts;
    console.log(resultts.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
