#!/usr/bin/node

exports.esrever = function (list) {
  const result = [];
  for (let i = list.length - 1; i >= 0; i--) {
    result[list.length - 1 - i] = list[i];
  }
  return result;
};
