#!/usr/bin/node
const list = require('./100-data');
const newlist = list.map((x, index) => x * index);
console.log(list);
console.log(newlist);
