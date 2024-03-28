#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(endpoint, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    getCharacters(data.characters, 0);
  }
});

function getCharacters (characters, idx) {
  request(characters[idx], function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      console.log(JSON.parse(response.body).name);
      if (idx + 1 < characters.length) {
        getCharacters(characters, idx + 1);
      }
    }
  });
}
