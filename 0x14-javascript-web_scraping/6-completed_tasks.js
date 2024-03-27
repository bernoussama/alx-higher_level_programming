#!/usr/bin/node

const request = require('request');

const endpoint = process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    for (const todo of data) {
      console.log(todo);
    }
  }
});
