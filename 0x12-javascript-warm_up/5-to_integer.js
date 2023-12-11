#!/usr/bin/node
const { argv } = require('node:process');
const myNumber = Number(argv[2]);
if (!isNaN(myNumber)) console.log(`My number: ${myNumber}`);
if (isNaN(myNumber)) console.log('Not a number');
