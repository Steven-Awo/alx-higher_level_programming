#!/usr/bin/node

exports.esrever = function (list) {
  let lengt = list.length - 1;
  let x = 0;

  while ((lengt - x) > 0) {
    const tempr = list[lengt];
    list[lengt] = list[x];
    list[x] = tempr;
    x++;
    lengt--;
  }
  return list;
};
