// Fetches data
import $ from 'jquery';
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  success: function (response) {
    const charName = response.name;
    $('#character').text(charName);
  }
});
