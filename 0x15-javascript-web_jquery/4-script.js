$(document).ready(function () {
  const btn = $('DIV#toggle_header');
  btn.click(function () {
    $('header').toggleClass('red green');
  });
});
