#!/usr/bin/node

const request = require('request');

const endpoint = process.argv[2];

const todos = {};
request(endpoint, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(response.body);
    for (const todo of data) {
      // console.log(todo);
      if (todo.completed === true) {
        const id = todo.userId.toString();
        if (id in todos) {
          todos[id] += 1;
        } else {
          todos[id] = 1;
        }
      }
    }
  }
  console.log(todos);
});
