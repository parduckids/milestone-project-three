// get the current year
const currentYear = new Date().getFullYear();

// user id "footer-year" and set its text content to the current year
document.getElementById("footer-year").textContent = "© " + currentYear + " Wave & Leaf";

// init Select2 multiple selection dropdown for allergens

$('#recipeAllergens').select2({
    // setting the placeholder when no option is selected
    placeholder: "Choose allergens contained in this recipe", 
    // clear the placeholder once there is an option selected
    allowClear: true 
});

// modal auth

// once the page is loaded successfully
$(document).ready(function () {
    checkLoginStatus();
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
        $.ajax({
            type: 'POST',
            url: '/logout',
            success: function(data) {
                window.location.href = data.redirect;  // Redirect to the URL provided by the server
                alert("Logged out successfully!");
            },
            error: function() {
                alert('Logout failed. Please try again.');
            }
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
                $('#uploadRecipeButton').show();
            } else {
                $('#registerButton').show();
                $('#loginButton').show();
                $('#logoutButton').hide();
                $('#welcomeMessage').hide();
                $('#uploadRecipeButton').hide();
            }
        });
    }
});