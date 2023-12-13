#!/usr/bin/node

let argnum = 0;
exports.logMe = function (item) {
  console.log(`${argnum}: ${item}`);
  argnum++;
  return argnum;
};
