const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});
