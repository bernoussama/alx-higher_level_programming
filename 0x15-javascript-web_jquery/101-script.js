#!/usr/bin/node

$("document").ready(() => {
  $("DIV#add_item").on("click", () => {
    $("UL.my_list").append("<li>Item</li>");
  });

  $("DIV#remove_item").on("click", () => {
    $("UL.my_list li:last-child").remove();
  });

  $("DIV#clear_list").on("click", () => {
    $("UL.my_list").empty();
  });
});
