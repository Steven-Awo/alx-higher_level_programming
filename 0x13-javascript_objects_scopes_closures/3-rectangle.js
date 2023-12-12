#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if ((h > 0) && (w > 0)) {
      this.width = w;
      this.height = h;
    } 
  }
  print () {
    for (let x = 0; x < this.height; x++) {
      let a = '';
      for (let y = 0; y < this.width; y++) {
        a += 'X';
      }
      console.log(a);
    }
  }
}

module.exports = Rectangle;
