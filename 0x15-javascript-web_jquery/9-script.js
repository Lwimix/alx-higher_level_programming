// fetches data
import $ from 'jquery';
$(document).ready(() => {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (response) {
      const text = response.hello;
      $('#hello').text(text);
    }
  });
});
