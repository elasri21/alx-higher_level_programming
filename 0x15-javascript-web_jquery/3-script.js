document.ready(function ($) {
  const btn = $('DIV#red_header');
  btn.click(function () {
    $('header').addClass('red');
  });
});
