#!/usr/bin/node

const fs = require('fs');

if (process.argv.length > 2) {
  const filename = process.argv[2];
  fs.readFile(filename, 'utf-8', function (err, data) {
    if (err) { throw err; }
    console.log(data);
  });
}
