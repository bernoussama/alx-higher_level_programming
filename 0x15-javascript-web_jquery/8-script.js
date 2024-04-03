#!/usr/bin/node

const link = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.get(link, (data) => {
  console.log(data);
  $("UL#list_movies").append(
    data.results.map((movie) => {
      return `<li> ${movie.title}</li>`;
    }),
  );
});
