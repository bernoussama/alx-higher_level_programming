#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(endpoint, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    for (const character of data.characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(response.body).name);
        }
      });
    }
  }
});
