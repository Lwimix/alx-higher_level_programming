// Adds the class red to header after clicking
import $ from 'jquery';
$(document).ready(() => {
  $('DIV#red_header').on('click', () => {
    $('header').addClass('red');
  });
});
