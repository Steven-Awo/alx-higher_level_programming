#!/usr/bin/node
function add (a, b) {
  const soln = a + b;
  console.log(soln);
}

add(Number(process.argv[2]), Number(process.argv[3]));
