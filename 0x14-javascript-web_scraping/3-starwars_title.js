#!/usr/bin/node

const request = require('request');
const episoddeNum = process.argv[2];
const APII_URL = 'https://swapi-api.hbtn.io/api/films/';

request(APII_URL + episoddeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const respPonseJSON = JSON.parse(body);
    console.log(respPonseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
