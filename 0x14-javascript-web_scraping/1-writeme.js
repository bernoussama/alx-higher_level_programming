#!/usr/bin/node

const fs = require('fs');

// Get the file path and string from command-line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error('Error occurred while writing to the file:', err);
  } else {
    console.log('String written to file successfully.');
  }
});
