#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const adata = read(fileA);
const bdata = read(fileB);

const cdata = adata + '' + bdata;

fs.writeFile(fileC, cdata.toString(), 'utf8', function (err) {
  if (err) {
    console.error(err);
  }
});

function read (filename) {
  const data = fs.readFileSync(filename, 'utf8');
  return data;
}
