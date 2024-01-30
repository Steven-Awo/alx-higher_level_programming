#!/usr/bin/node

const reqts = require('request');

const idd = process.argv[2];

const urll = 'https://swapi-api.hbtn.io/api/films/';

reqts.get(urll + idd, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const datta = JSON.parse(body);

  const ddt = datta.characters;
  for (const x of ddt) {
    reqts.get(x, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const datta1 = JSON.parse(body1);
      console.log(datta1.name);
    });
  }
});
