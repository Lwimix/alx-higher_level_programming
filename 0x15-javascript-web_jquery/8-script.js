// Fetches data
$(document).ready(() => {
	$.ajax({
		url: "https://swapi-api.alx-tools.com/api/films?format=json",
		method: 'GET',
		success: function(response) {
			let films = response.results;
			let listFilms = $("#list_movies");
			films.forEach(function(film) {
				let title = film.title;
				listFilms.append("<li>" + title + "<li>");
			});
		}
	});
});
