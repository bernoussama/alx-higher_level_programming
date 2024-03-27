#!/usr/bin/node

const { warn } = require('console');
const fs = require('fs');
const { exit } = require('process');
const request = require('request');

// Get the file path and string from command-line arguments
const link = process.argv[2];
const filePath = process.argv[3];

request(link, (err, res, body) => {
  if (err) {
    console.error(err);
    exit();
  } else {
    // Write the string to the file in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
