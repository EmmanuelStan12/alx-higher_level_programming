#!/usr/bin/node

const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    const chr = c || 'X';
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += chr;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
