// Fetches data
import $ from 'jquery';
$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films?format=json',
    method: 'GET',
    success: function (response) {
      const films = response.results;
      const listFilms = $('#list_movies');
      films.forEach(function (film) {
        const title = film.title;
        listFilms.append('<li>' + title + '<li>');
      });
    }
  });
});
