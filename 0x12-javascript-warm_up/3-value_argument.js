#!/usr/bin/node
const { argv } = require('process');

argv[2] != undefined ? console.log(argv[2]) : console.log('No argument');
