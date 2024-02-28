document.addEventListener('DOMContentLoaded', function() {
  $(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
      const lang = $('INPUT#language_code').val();
      $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', function (data) {
	if (data.code == lang) {
          $('DIV#hello').text(data.hello);
	}
      });
    });
  });
});
