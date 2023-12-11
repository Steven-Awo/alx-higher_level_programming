#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const a = Number(process.argv[2]);
  let x = 0;
  while (x < a) {
    console.log('X'.repeat(a));
    x++;
  }
}
