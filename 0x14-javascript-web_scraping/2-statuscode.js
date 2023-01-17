#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request(url, function (err, response, body) {
    if (err) throw err;
    console.log('code: ' + response.statusCode);
  });
}
