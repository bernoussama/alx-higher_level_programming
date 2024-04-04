#!/usr/bin/node
$(document).ready(() => {
  //
  $("INPUT#btn_translate").click(() => {
    const link = `https://hellosalut.stefanbohacek.dev/?lang=${$("INPUT#language_code").val()}`;
    $.get(link, (data) => {
      console.log(data);
      $("DIV#hello").text(data.hello.toString());
    });
  });
});
