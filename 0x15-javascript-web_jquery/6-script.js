document.ready(function ($) {
  const btn = $('DIV#update_header');
  btn.click(function () {
    $('header').text('New Header!!!');
  });
});
