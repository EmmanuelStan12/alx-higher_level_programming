#!/usr/bin/node

const dict = require('./101-data').dict;
const result = {};
Object.entries(dict).forEach((arr) => {
  if (result[arr[1]]) {
    result[arr[1]].push(arr[0]);
  } else {
    result[arr[1]] = [arr[0]];
  }
});
console.log(result);
