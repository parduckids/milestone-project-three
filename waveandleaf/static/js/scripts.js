// get the current year
const currentYear = new Date().getFullYear();

// user id "footer-year" and set its text content to the current year
document.getElementById("footer-year").textContent = "© " + currentYear + " Wave & Leaf";



// modal auth

// once the page is loaded successfully
$(document).ready(function() {
    // use ajax post request to the /register route that's created with flask
    $('#registrationModal .btn-success').click(function() {
        var username = $('#registrationModal #username').val();
        var password = $('#registrationModal #password').val();
        $.ajax({
            type: 'POST',
            url: '/register',
            data: {
                username: username,
                password: password
            },
            // hide modal and show alert if successful registration
            success: function(response) {
                alert(response.message);
                $('#registrationModal').modal('hide');
            },
            error: function(xhr, status, error) {
                // check if responseJSON is defined, use jsonified message that flask sends
                if(xhr.responseJSON && xhr.responseJSON.error){
                    alert(xhr.responseJSON);
                } else {
                    // general error message or parse the status or error thrown by jQuery
                    alert('Failed to register: ' + error);
                }
            }
        });
    });
    // use ajax post request to the /login route that's created with flask
    $('#loginModal .btn-outline-success').click(function() {
        var username = $('#loginModal #loginUsername').val();
        var password = $('#loginModal #loginPassword').val();
        $.ajax({
            type: 'POST',
            url: '/login',
            data: {
                username: username,
                password: password
            },
            // hide modal and show alert if successful registration
            success: function(response) {
                alert(response.message);
                $('#loginModal').modal('hide');
                // optionally, redirect to another page or update UI
            },
            error: function(xhr, status, error) {
                // check if responseJSON is defined, use jsonified message that flask sends
                if(xhr.responseJSON && xhr.responseJSON.error){
                    alert(xhr.responseJSON.error);
                } else {
                    // general error message or parse the status or error thrown by jQuery
                    alert('Login failed: ' + error);
                }
            }
        });
    });
});
