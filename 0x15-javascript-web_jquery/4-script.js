// Toggles classes
import $ from 'jquery';
$(document).ready(() => {
  $('DIV#toggle_header').on('click', () => {
    $('header').toggleClass('red green');
  });
});
