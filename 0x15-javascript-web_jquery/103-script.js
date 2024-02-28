document.addEventListener('', function () {
  $(document).ready(function () {
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function (e) {
      if (e.which === 13) {
        fetchTranslation();
      }
    });

    function fetchTranslation () {
      const languageCode = $('#language_code').val();
      $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
        .done(function (data) {
          $('#hello').text(data.hello);
        })
        .fail(function () {
          $('#hello').text('Translation not available');
        });
    }
  });
});
