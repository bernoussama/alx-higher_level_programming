#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
Object.entries(dict).forEach(([key, value]) => {
  if (newDict[value] === undefined) {
    newDict[value] = [];
  }
  newDict[value].push(key);
});
