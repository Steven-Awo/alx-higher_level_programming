#!/usr/bin/node

let numbofarg = 0;

exports.logMe = function (item) {
  console.log(numbofarg + ': ' + item);
  numbofarg++;
};
