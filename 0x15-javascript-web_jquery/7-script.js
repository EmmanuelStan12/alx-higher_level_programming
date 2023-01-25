const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(function () {
	$.get(url, function(data, textStatus) {
		$('DIV#character').text(data['name']);
	})
});
