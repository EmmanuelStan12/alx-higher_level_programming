#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
  const url = endpoint + movieId;
  request.get(url, function (err, response, body) {
    if (err) throw err;
    const data = JSON.parse(body);
    console.log(data.title);
  });
}
