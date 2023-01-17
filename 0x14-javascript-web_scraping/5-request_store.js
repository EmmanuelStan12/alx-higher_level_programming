#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length > 3) {
  const url = process.argv[2];
  const filename = process.argv[3];
  request.get(url, function (err, response, body) {
    if (err) throw err;
    fs.writeFile(filename, body, 'utf-8', function (err) {
      if (err) throw err;
    });
  });
}
