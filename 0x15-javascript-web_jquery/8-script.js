document.ready(function ($) {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const tiltes = data.title;
    filmTitles = $('UL#list_movies');
    titles.each(title => {
      filmTitles.append(`<li>${title}</li>`);
    });
  });
});
