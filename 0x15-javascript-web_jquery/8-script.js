const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(function () {
  $.get(url, function (data, textStatus) {
    data.results.forEach((movie) => {
      const el = '<li>' + movie.title + '</li>';
      $('UL#list_movies').append(el);
    });
  });
});
