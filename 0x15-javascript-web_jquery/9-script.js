#!/usr/bin/node
$(document).ready(() => {
  //
  const link = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  $.get(link, (data) => {
    $("DIV#hello").text(data.hello);
  });
});
