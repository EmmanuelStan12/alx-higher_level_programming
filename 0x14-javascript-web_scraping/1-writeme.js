#!/usr/bin/node

const fs = require('fs');

if (process.argv.length > 3) {
  const filename = process.argv[2];
  const data = process.argv[3];
  fs.writeFile(filename, data, 'utf-8', function (err) {
    if (err) throw err;
  });
}
