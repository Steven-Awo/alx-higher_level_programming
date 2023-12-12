#!/usr/bin/node

const dictry = require('./101-data').dict;

const total_list = Object.entries(dictry);

const valus = Object.values(dictry);

const valusUniq = [...new Set(valus)];

const newrDictry = {};

for (const x in valusUniq) {
  const listts = [];
  for (const y in total_list) {
    if (total_list[y][1] === valusUniq[x]) {
      listts.unshift(total_list[y][0]);
    }
  }
  newrDictry[valusUniq[x]] = listts;
}
console.log(newrDictry);
