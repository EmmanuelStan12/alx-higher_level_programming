#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const target = process.argv[4];

fs.readFile(fileA, function (err, dataA) {
  if (!err) {
    fs.readFile(fileB, function (err, dataB) {
      if (!err) {
        const result = dataA + dataB;
        fs.writeFile(target, result, function (err) {
          if (err) {
            console.log(err);
          }
        }
        );
      }
    });
  }
});
