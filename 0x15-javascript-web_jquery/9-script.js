// fetches data
$(document).ready(() => {
	$.ajax({
		url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
		method: "GET",
		success: function(response) {
			let text = response.hello;
			$("#hello").text(text);
		}
  });
});
