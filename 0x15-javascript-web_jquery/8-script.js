$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const titles = data.results;
    filmTitles = $('UL#list_movies');
    titles.forEach(title => {
      filmTitles.append(`<li>${title.title}</li>`);
    });
  });
});
