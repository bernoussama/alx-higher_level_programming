#!/usr/bin/node

const request = require('request');

const endpoint = process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    const filtered = data.results.filter((movie) =>
      movie.characters.find((character) => character.includes('18'))
    );
    console.log(filtered.length);
  }
});
