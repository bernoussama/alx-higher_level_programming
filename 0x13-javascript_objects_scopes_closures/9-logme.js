#!/usr/bin/node
exports.logMe = function (item) {
  let argnum = 0;

  return function (item) {
    console.log(`${argnum}: ${item}`);
    argnum++;
  };
};
