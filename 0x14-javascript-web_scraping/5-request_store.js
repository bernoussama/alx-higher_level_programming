#!/usr/bin/node

const fs = require('fs');
const { exit } = require('process');
const request = require('request');

// Get the file path and string from command-line arguments
const link = process.argv[2];
const filePath = process.argv[3];

const content = () => {
  const html = '';
  request(link, (err, res, body) => {
    if (err) {
      console.error(err);
      exit();
    } else {
      console.log(body);
      html = body;
    }
  });
  return html;
};

// Write the string to the file in UTF-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
