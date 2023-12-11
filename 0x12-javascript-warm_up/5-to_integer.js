#!/usr/bin/node
const { argv } = require('node:process');

const myNumber = +argv[2];
if (!isNaN(myNumber)) console.log(`My number: ${myNumber}`);
if (isNaN(myNumber)) console.log('Not a number');
