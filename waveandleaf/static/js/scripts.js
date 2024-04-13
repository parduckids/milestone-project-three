// get the current year
const currentYear = new Date().getFullYear();

// user id "footer-year" and set its text content to the current year
document.getElementById("footer-year").textContent = "© " + currentYear + " Wave & Leaf";



// modal auth

// once the page is loaded successfully
$(document).ready(function () {
    // use ajax post request to the /register route that's created with flask
    $('#registrationModal .btn-success').click(function () {
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
            success: function (response) {
                alert(response.message);
                $('#registrationModal').modal('hide');
            },
            error: function (xhr, status, error) {
                // check if responseJSON is defined, use jsonified message that flask sends
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    alert(xhr.responseJSON.error);
                } else {
                    // general error message or parse the status or error thrown by jQuery
                    alert('Failed to register: ' + error);
                }
            }
        });
    });
    // use ajax post request to the /login route that's created with flask
    $('#loginModal .btn-outline-success').click(function () {
        var username = $('#loginModal #loginUsername').val();
        var password = $('#loginModal #loginPassword').val();
        $.ajax({
            type: 'POST',
            url: '/login',
            data: {
                username: username,
                password: password
            },
            success: function (response) {
                alert(response.message);
                $('#loginModal').modal('hide');
                // call this function to update UI based on login status
                checkLoginStatus();

            },
            error: function (xhr) {
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    alert(xhr.responseJSON.error);
                } else {
                    alert('Login failed: ' + xhr.statusText);
                }
            }
        });
    });

    // log out function, when logout button clicked use the flask /logout route to log out 
    $('#logoutButton').click(function () {
        $.post('/logout', function (response) {
            alert('Logged out successfully');
            // update UI to reflect logged-out status
            checkLoginStatus();
        });
    });

    // modify the ui depending on if the user is logged in or not
    function checkLoginStatus() {
        $.get('/check-login', function (response) {
            if (response.logged_in) {
                $('#registerButton').hide();
                $('#loginButton').hide();
                $('#logoutButton').show();
                $('#welcomeMessage').show();
                $('#usernameSpan').text(response.username);
            } else {
                $('#registerButton').show();
                $('#loginButton').show();
                $('#logoutButton').hide();
                $('#welcomeMessage').hide();
            }
        });
    }
});