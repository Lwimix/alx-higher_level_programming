// Updates header color and adds event
import $ from 'jquery';
$(document).ready(() => {
  $('DIV#red_header').on('click', () => {
    $('header').css('color', 'red');
  });
});
