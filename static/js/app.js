$('#contactForm').on('submit', function(e) {

	//prevent submit event from automattically submitting the form
	e.preventDefault();

	//call ajax on the server to initialize the ephone call

	$.ajax({
		url: '/call',
		method: 'POST',
		dataType: 'json',
		data: {
			phoneNumber: $('#phoneNumber').val()
		}
	}).done(function(data) {
		//the JSON set back will contain a success message
		alert(data.message;)
	}).fail(function(error) {
		alert(JSON.stringify(error));
	});
});