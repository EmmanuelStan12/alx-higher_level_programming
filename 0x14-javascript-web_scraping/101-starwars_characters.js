#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const endpoint = 'https://swapi-api.alx-tools.com/api/films/';
  const url = endpoint + movieId;
  const result = {};
  request.get(url, function (err, response, body) {
    if (err) throw err;
    const data = JSON.parse(body);
    data.characters.forEach((ch, i) => {
      request.get(ch, function (e, res, b) {
        if (e) throw e;
        result[i] = JSON.parse(b).name;
        if (Object.keys(result).length === data.characters.length) {
          for (const p in result) {
            console.log(result[p]);
          }
        }
      });
    });
  });
}
