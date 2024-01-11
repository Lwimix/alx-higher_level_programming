// Replaces text in element
import $ from 'jquery';
$(document).ready(() => {
  $('DIV#update_header').on('click', () => {
    $('header').text('New Header!!!');
  });
});
