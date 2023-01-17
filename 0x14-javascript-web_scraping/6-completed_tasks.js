#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const url = process.argv[2];
  const result = {};
  request.get(url, function (err, response, body) {
    if (err) throw err;
    const data = JSON.parse(body);
    for (const todo of data) {
      if (todo.completed) {
        if (result[todo.userId]) {
          const c = result[todo.userId];
          result[todo.userId] = c + 1;
          continue;
        }
        result[todo.userId] = 1;
      }
    }
    console.log(result);
  });
}
