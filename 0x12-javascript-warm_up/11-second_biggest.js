#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const darray = process.argv.slice(2).map(Number);
  const secnd = darray.sort(function (x, y) { return y - x; })[1];
  console.log(secnd);
}
