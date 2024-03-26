#!/usr/bin/node

const request = require('request');

const link = process.argv[2];

request(link, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
