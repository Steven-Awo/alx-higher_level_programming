#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const y = Number(process.argv[2]);
  let x = 0;
  while (x < y) {
    console.log('C is fun');
    x++;
  }
}
