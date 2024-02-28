document.ready(function ($) {
  const btn = $('DIV#red_header');
  btn.click(function () {
    if ($('header').has('green')) {
      $('header').className = 'red';
    } else {
      $('header').className = 'green';
    }
  });
});
