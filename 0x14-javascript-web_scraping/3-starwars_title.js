#!/usr/bin/node

const request = require('request');

const episodeNum = process.argv[2];

const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + episodeNum, function (errr, response, body) {
  if (errr) {
    console.log(errr);
  }
  else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  }
  else {
    console.log('Error code: ' + response.statusCode);
  }
});

