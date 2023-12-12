#!/usr/bin/node

exports.converter = function (base) {
  return function (numbr) {
    return numbr.toString(base);
  };
};
