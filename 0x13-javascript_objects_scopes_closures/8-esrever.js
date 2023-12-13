#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  list.forEach((element) => tsil.unshift(element));
  return tsil;
};
