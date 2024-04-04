#!/usr/bin/node
$(document).ready(() => {
  //
  $("INPUT#language_code").on("focus", () => {
    $("INPUT#language_code").on("keydown", (e) => {
      if (e.originalEvent.which === 13) {
        $("INPUT#btn_translate").trigger("click");
      }
    });
  });

  $("INPUT#btn_translate").click(() => {
    const link = `https://hellosalut.stefanbohacek.dev/?lang=${$("INPUT#language_code").val()}`;
    $.get(link, (data) => {
      console.log(data);
      $("DIV#hello").text(data.hello.toString());
    });
  });
});
