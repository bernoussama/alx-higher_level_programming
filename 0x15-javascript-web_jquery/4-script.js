#!/usr/bin/node

$("DIV#toggle_header").on("click", () => {
  $("header").toggleClass("red green");
});
