// loading screen
showLoading()
// show loading overlay
function showLoading() {
    document.getElementById('loading-overlay').style.display = 'block';
}

// hide loading overlay
function hideLoading() {
    // Fade out the loading overlay
    $('#loading-overlay').fadeOut('slow');
}

// listen for the page load event
window.addEventListener('load', function () {
    // hide loading overlay when the page has finished loading
    hideLoading();
});


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
                Swal.fire({
                    title: response.message,
                    icon: "success"
                });
                $('#registrationModal').modal('hide');
            },
            error: function (xhr, status, error) {
                // check if responseJSON is defined, use jsonified message that flask sends
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    Swal.fire({
                        title: xhr.responseJSON.error,
                        icon: "error"
                    });
                } else {
                    // general error message or parse the status or error thrown by jQuery
                    Swal.fire({
                        title: 'Failed to register: ' + error,
                        icon: "error"
                    });
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
                // add confirmation
                Swal.fire({
                    title: response.message,
                    icon: "success"
                });
                // call this function to update UI based on login status
                checkLoginStatus();

            },
            error: function (xhr) {
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    Swal.fire({
                        title: xhr.responseJSON.error,
                        icon: "error"
                    });

                } else {
                    Swal.fire({
                        title: 'Login failed: ' + xhr.statusText,
                        icon: "error"
                    });

                }
            }
        });
    });

    // log out function, when logout button clicked use the flask /logout route to log out 
    $('#logoutButton').click(function () {
        $.ajax({
            type: 'POST',
            url: '/logout',
            success: function (data) {
                Swal.fire({
                    title: "Logged out successfully!",
                    icon: "success"
                }).then((result) => {
                    // check if the user confirmed the SweetAlert
                    if (result.isConfirmed) {
                        // redirect to the URL provided by the server after user alert
                        window.location.href = data.redirect;
                    }
                });
            },
            error: function () {
                Swal.fire({
                    title: "Logout failed. Please try again.",
                    icon: "error"
                });
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
                $('#myRecipesButton').show();
            } else {
                $('#registerButton').show();
                $('#loginButton').show();
                $('#logoutButton').hide();
                $('#welcomeMessage').hide();
                $('#uploadRecipeButton').hide();
                $('#myRecipesButton').hide();
            }
        });
    }
    // add sweetalert error message when a recipe is not available using url params
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('error') === 'norecipe') {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'The recipe you are looking for does not exist!'
        });
    }

    // delete recipe alert for myrecipes page:
    $('.deleteForm').on('submit', function (e) {
        e.preventDefault(); // Prevent the form from submitting through HTML form submission
        var form = this; // 'this' refers to the form element

        Swal.fire({
            title: 'Are you sure?',
            text: 'Do you want to delete this recipe?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#496989',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!',
            cancelButtonText: 'No, cancel!'
        }).then((result) => {
            if (result.isConfirmed) {
                form.submit(); // Submit the form programmatically
            }
        });
    });

    // edit recipe alert for edit recipe page:
    $('.editForm').on('submit', function (e) {
        e.preventDefault(); // Prevent the form from submitting through HTML form submission
        var form = this; // 'this' refers to the form element

        Swal.fire({
            title: 'Are you sure?',
            text: 'Do you want to save the changes for this recipe?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#496989',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, save the changes!',
            cancelButtonText: 'No, cancel!'
        }).then((result) => {
            if (result.isConfirmed) {
                form.submit(); // Submit the form programmatically
            }
        });
    });

    // upload recipe alert for upload recipe page:
    $('.uploadForm').on('submit', function (e) {
        e.preventDefault(); // Prevent the form from submitting through HTML form submission
        var form = this; // 'this' refers to the form element

        Swal.fire({
            title: 'Are you sure?',
            text: 'Do you want to upload this recipe?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonColor: '#496989',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, upload it now!',
            cancelButtonText: 'No, cancel!'
        }).then((result) => {
            if (result.isConfirmed) {
                form.submit(); // Submit the form programmatically
            }
        });
    });

});