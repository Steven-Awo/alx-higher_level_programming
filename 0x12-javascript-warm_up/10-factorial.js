#!/usr/bin/node
function factorl (numb) {
  if (numb < 0) {
    return (-1);
  }
  if (numb === 0 || isNaN(numb)) {
    return (1);
  }
  return (numb * factorl(numb - 1));
}

console.log(factorl(Number(process.argv[2])));
