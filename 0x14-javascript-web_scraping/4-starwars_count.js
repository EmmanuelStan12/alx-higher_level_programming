#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  request.get(url, function (err, response, body) {
    if (err) throw err;
    const data = JSON.parse(body);
    const results = data.results;
    const count = results.reduce(function (acc, movie) {
      for (const c of movie.characters) {
        if (c.includes('18')) {
          return (acc + 1);
        }
      }
      return acc;
    }, 0);
    console.log(count);
  });
}
