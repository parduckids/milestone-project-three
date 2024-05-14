

# Testing the Wave & Leaf webapp 

##  Content

- [User Story Testing](#user-story-testing)
    + [New Visitor](#new-visitor)
    + [Registered User](#registered-user)
    + [Recipe Contributor](#recipe-contributor)
    + [Food Enthusiast](#food-enthusiast)
    + [Site Administrator](#site-administrator)
- [Compatibility Testing](#compatibility-testing)
    + [Device Compatibility Testing](#device-compatibility-testing)
    + [Browser Compatibility Testing](#browser-compatibility-testing)
- [Code Review & Validation](#code-review-and-validation)
    + [HTML Validation](#html-validation)
    + [CSS Validation](#css-validation)
    + [Javascript Validation](#javascript-validation)
    + [Python Validation](#python-validation)
- [Bugs & Issues](#bugs-and-issues)
    + [Fixed](#fixed)
    + [Unfixed](#unfixed)
- [Color Contrast Testing](#color-contrast-testing)
    + [Navigation & Footer](#navigation-bar-and-footer)
    + [Rest of the site](#rest-of-the-site)
- [Manual Testing](#manual-testing)
- [LightHouse Testing](#lighthouse-testing)


# User Story Testing

## New Visitor

### As a new visitor, I want to easily navigate the website and understand its purpose from the homepage so I can quickly decide if it meets my needs.
* The homepage features a welcoming design with three image bubbles representing vegan, vegetarian, and pescatarian recipes. Clicking on these bubbles takes the user to the respective category pages where they can browse recipes. The navigation bar includes links to the Home, About Us, and Recipes pages, as well as Register and Login buttons. The footer contains the current year, app name, logo, and a GitHub link.

### As a new visitor, I want to be able to browse recipes without registering to see if the site has the types of recipes I'm interested in.
* Visitors can browse recipes by clicking on the image bubbles on the homepage or by using the Recipes dropdown in the navigation bar, which offers options for vegan, vegetarian, and pescatarian recipes. These actions lead to category pages displaying recipe cards with titles, images, and brief descriptions.

## Registered User

### As a registered user, I want to easily register and log in to the site so I can start uploading and managing my recipes.
* The Register and Login buttons in the navigation bar trigger popups where users can register or log in using styled SweetAlert2 alerts for confirmation messages. After logging in, the navigation bar updates to replace the Register and Login buttons with Upload Recipe and My Recipes links.

### As a registered user, I want to upload recipes under specific dietary categories (vegan, vegetarian, pescatarian) with details like allergens, difficulty, and cooking time to help others make informed decisions.
* The Upload Recipe page features a comprehensive form where users can enter recipe details, including dietary category, allergens, difficulty level, and cooking time. The form also supports image uploads via Cloudinary, allowing users to upload images from their camera, via a link, or by uploading a file.

### As a registered user, I want to edit or delete my recipes after they are posted if I need to update or correct information.
* The My Recipes page displays a list of recipes uploaded by the user. Each recipe card includes options to view, edit, or delete the recipe. Users can update the recipe details or remove the recipe entirely, with confirmation alerts ensuring that actions are intentional.

### As a registered user, I want to receive clear confirmation alerts after performing actions (like uploading, editing, or deleting recipes) to ensure that my changes have been successfully applied.
* After performing actions such as uploading, editing, or deleting a recipe, users receive clear confirmation messages via styled SweetAlert2 alerts, confirming the success of their actions.

## Recipe Contributor

### As a recipe contributor, I want to include detailed descriptions, ingredients lists, and step-by-step cooking instructions in my recipe uploads to provide clear guidance to others.
* The recipe upload form allows contributors to provide detailed descriptions, ingredient lists, and step-by-step instructions. These details are displayed on the recipe page, offering clear guidance to other users.

### As a recipe contributor, I need to be able to list my name as the creator and track when my recipes were uploaded or last edited for my own records.
* Each recipe displays the creator's name and includes timestamps for when the recipe was uploaded and last edited. This information is visible on the recipe page and the My Recipes page.

### As a recipe contributor, I want to upload images of my cooking directly from my camera, via a link, or by uploading a file, to share my culinary creations with the community.
* The Upload Recipe page supports multiple image upload methods through Cloudinary, including direct uploads from a camera, via a URL, or by file upload. These images are displayed prominently on the recipe page.

## Food Enthusiast

### As a food enthusiast, I want to browse recipes by dietary category and view images associated with each recipe, allowing me to visually select dishes that appeal to me.
* Users can browse recipes by dietary category through the Recipes dropdown in the navigation bar or by clicking on the image bubbles on the homepage. Each recipe card includes an image, title, and brief description, making it easy to visually select appealing dishes.

## Site Administrator

### As a site administrator, I want to ensure that users can only perform CRUD (create, read, update, delete) operations on recipes they have uploaded themselves to maintain privacy and control over content.
* Permissions are in place to ensure that users can only edit or delete their own recipes.

# Compatibility Testing

## Device Compatibility Testing

### Responsiveness
* Responsiveness tests were done, using Google Chrome Developer Tools across different device screen sizes, including:

- iPhone SE
- iPhone XR
- iPhone 12 Pro
- Pixel 5
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- iPad Mini
- iPad Air
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/A71

Additionally, I tested the website on the following physical devices:

- iPhone 12 mini
- Nokia G22
- iPad Pro M3 
- Dell 17" laptop
- Macbook Pro 16"
- Samsung widescreen monitor


## Browser Compatibility Testing

The site was tested across different browsers to check compatibility:

- **Desktop Browsers:**
  - Google Chrome (Windows and Mac OS)
  - Microsoft Edge (Windows and Mac OS)
  - Mozilla Firefox
  - Opera
  - Brave

- **Mobile and Tablet Browsers:**
  - Google Chrome (Android)
  - Safari (iOS)
  - DuckDuckGo (iOS)
  - Microsoft Edge (iOS)
  - Mozilla Firefox (iOS)

No issues were encountered during browser testing.

## Color Contrast Testing 

### Navigation bar and Footer
![image](/waveandleaf/static/readme/navbar-footer-colors.png)

### Rest of the site:

* Using #fff and #000 which are working well together
* Some buttons are using ligter colors but those are well visible on every page

## Code Review and Validation

### HTML Validation
* The HTML code was reviewed using the W3C Markup Validation Service. This review process ensured that the HTML structure adheres to current web standards, improving cross-browser compatibility and overall site performance. All identified issues were corrected .

* Home page:<br>
![image](/waveandleaf/static/readme/html-test-home.png)
* About page:<br>
![image](/waveandleaf/static/readme/html-test-about.png)
* Recipe Category page:<br>
![image](/waveandleaf/static/readme/html-test-recipe-category.png)
* Recipe Page:<br>
![image](/waveandleaf/static/readme/html-test-recipe.png)

### CSS Validation
* The CSS code was reviewed using the W3C CSS Validation Service. This process confirmed that all CSS rules are correctly defined and conform to the latest CSS specifications.

The CSS code was reviewed using the W3C CSS Validation Service. The validation process confirmed that all CSS rules are correctly defined and conform to the latest CSS specifications.<br>

![image](/waveandleaf/static/readme/css-testing.png)

#### Note on External CSS Libraries

```.fa-rotate-by var(--fa-rotate-angle, none) is not a transform value: rotate(var(--fa-rotate-angle, none)) ```

**This error originates from the Font Awesome CSS file loaded via CDN. Since this file is a third-party library and not part of the custom-written CSS for the project, this error does not reflect an issue with the project's CSS code. The project's own CSS files passed the validation without any errors.**

### JavaScript Validation
* JavaScript code was reviewed using ESLint, a popular linting utility for JavaScript. The code was checked to follow best practices and avoid potential errors. Any issues identified were fixed, resulting in cleaner and more maintainable code.

![image](/waveandleaf/static/readme/jslint-pass.png)

### Python Validation
* Python code was reviewed using Pylint and Flake8, two widely used linting tools. These tools checked for syntax errors, code quality issues, and PEP 8 standards. Reported issues were fixed, ensuring that the code is clean, efficient, and follows Python best practices.


# Bugs and Issues


## Fixed

* **HTML validation:** missing image link:<br>
![image](/waveandleaf/static/readme/missing-link-html.png)
**[Fixed on commit: 5b4c31e](https://github.com/parduckids/milestone-project-three/commit/5b4c31e3a348ebfffaba57d8d7124ba284bf85e7)** 

* **JS validation:** 'result' is defined but never used:<br>
![image](/waveandleaf/static/readme/jslint-error.png)
**[Fixed on commit: 5b4c31e](https://github.com/parduckids/milestone-project-three/commit/d867822b89ea39b2320e305fdaee92cdd26f1a00)**

* **Python validation:** Almost all of these issues were fixed some aren't (see Unfixed issues)<br>
    * ``` run.py ```
![image](/waveandleaf/static/readme/run-testing.png)
    * ``` models.py ```
![image](/waveandleaf/static/readme/models-testing.png)
    * ``` routes.py ```
![image](/waveandleaf/static/readme/routes-testing.png)

**[Fixed on commit: 15baf6d](https://github.com/parduckids/milestone-project-three/commit/15baf6d83a6ba50de1af457265f99f043cf1ceea)**

## Unfixed

* **Python validation:**

### Explanation for Remaining Flake8 Issues<br>
![image](/waveandleaf/static/readme/routes-testing-fixed.png)<br>
![image](/waveandleaf/static/readme/models-testing-fixed.png)

#### `waveandleaf/routes.py`

1. **F401: Unused Import**
   - **Reason**: `DifficultyLevel` is imported but not used.
   - **Left In**: Could be required for future enhancements or planned features.

2. **F841: Unused Variable**
   - **Reason**: `category` is assigned but not used.
   - **Left In**: The variable might be part of an incomplete feature or necessary for maintaining code logic clarity.

3. **E501: Line Too Long**
   - **Reason**: Line exceeds 79 characters.
   - **Left In**: Splitting lines might reduce readability or break complex expressions.

#### `waveandleaf/models.py`

1. **E501: Line Too Long**
   - **Reason**: Line exceeds 79 characters.
   - **Left In**: Splitting lines might reduce readability or break complex expressions.

These issues are minor and do not affect code functionality but should be reviewed for cleanup.



# Manual Testing

## Navigation Bar
* **Navigation Bar when the user isn't logged in:**
    * Log in and Register buttons were tested and function correctly.
    * ![image](/waveandleaf/static/readme/navbar-basic.png)
* **Navigation Bar when the user is logged in:**
    * Log in and Register buttons are hidden; My Recipes and Upload Recipe buttons, and "Hey 'username'" text are present and functioning correctly.
    * ![image](/waveandleaf/static/readme/navbar-logged-in.png)
* **Navigation Bar on mobile and tablet:**
    * Navigation functionality was tested on mobile and tablet devices.
    * ![image](/waveandleaf/static/readme/navbar-mobile.png)
* **Navigation Bar on mobile and tablet when the user isn't logged in:**
    * Log in and Register buttons are present and function correctly.
    * ![image](/waveandleaf/static/readme/navbar-mobile-basic.png)
* **Navigation Bar on mobile and tablet when the user is logged in:**
    * Log in and Register buttons are hidden; My Recipes and Upload Recipe buttons, and "Hey 'username'" text are present and functioning correctly.
    * ![image](/waveandleaf/static/readme/navbar-mobile-logged-in.png)

## Footer
* **Footer:**
    * Name, current year (via JS function), logo (redirects to home page), and GitHub icon link were tested and work correctly.
    * ![image](/waveandleaf/static/readme/footer.png)
* **Footer on mobile and tablet:**
    * Footer functionality was tested on mobile and tablet devices.
    * ![image](/waveandleaf/static/readme/footer-mobile.png)

## Authentication
* **Register:**
    * Registration modal with Bootstrap was tested for functionality including placeholder text, labels, and close button.
    * ![image](/waveandleaf/static/readme/registration.png)
* **Log In:**
    * Log in modal with Bootstrap was tested for functionality including placeholder text, labels, and close button.
    * ![image](/waveandleaf/static/readme/login.png)

## CRUD Operations
* **Create Recipe:**
    * Upload Recipe button appears once the user is logged in and functions correctly.
    * ![image](/waveandleaf/static/readme/upload-button.png)
    * Upload recipe form entries were tested, including:
        * Recipe title
        * Recipe category dropdown (vegan, vegetarian, pescatarian)
        * Recipe difficulty dropdown (easy, medium, hard)
        * Cooking time (user indicates minutes or hours, can add extra notes)
        * Serving size (number field)
        * Recipe description
        * Ingredients (separated with commas for an unordered list)
        * Instructions (step-by-step guide, separated by pressing enter after each step)
        * Allergens (multiple selection field using Select2 jQuery plugin)
        * Upload image button (triggers Cloudinary for multiple upload methods)
            * Verified default image is used if no image is provided.
            * ![image](https://i.ibb.co/kBz5npG/This-dish-disappeared-too-quickly-for-a-photoshoot.png)
    * ![image](/waveandleaf/static/readme/upload-recipe.gif)

* **Read Recipes:**
    * Recipe pages are accessible to all users, logged in or not.
    * Recipes can be accessed from category pages or the My Recipes page (for logged-in users) using the 'Go to the Recipe' button.
    * ![image](/waveandleaf/static/readme/recipe.gif)
    * ![image](/waveandleaf/static/readme/goto.png)

* **Update Recipe:**
    * Edit Recipe page is accessible only to logged-in users and functions correctly.
    * Fields are prepopulated with existing values for easier updates.
    * Image can only be changed via a link (Cloudinary not available in edit mode).
    * Users must confirm changes before saving.
    * ![image](/waveandleaf/static/readme/edit-recipe.gif)
    * ![image](/waveandleaf/static/readme/how-to-edit.png)

* **Delete Recipe:**
    * Delete Recipe functionality is accessible only to logged-in users and works correctly.
    * Users must confirm before deleting a recipe.
    * ![image](/waveandleaf/static/readme/how-to-edit.png)

## User Confirmations
* **User Registered:**
    * Registration confirmation pop-up tested and works correctly.
    * ![image](/waveandleaf/static/readme/registered-confirmation.png)
* **User Logged In:**
    * Log in confirmation pop-up tested and works correctly.
    * ![image](/waveandleaf/static/readme/logged-in-confirmation.png)
* **User Logged Out:**
    * Log out confirmation pop-up tested and works correctly.
    * ![image](/waveandleaf/static/readme/logged-out-confirmation.png)
* **User Uploading a New Recipe:**
    * Upload recipe confirmation pop-up tested and works correctly.
    * ![image](/waveandleaf/static/readme/upload-recipe-confirmation.png)
* **User Editing a Recipe:**
    * Edit recipe confirmation pop-up tested and works correctly.
    * ![image](/waveandleaf/static/readme/edit-recipe-confirmation.png)
* **User Deleting a Recipe:**
    * Delete recipe confirmation pop-up tested and works correctly.
    * ![image](/waveandleaf/static/readme/delete-recipe-confirmation.png)

* **My Recipes:**
    * 'My Recipes' button appears once the user is logged in.
    * Confirmed the button correctly forwards the user to their own recipe collection.
    * Users can view, edit, and delete their own recipes.
    * Edit and delete buttons are only available on the user's recipe collection page.
    * Recipe cards show the category name, and clicking the category name forwards the user to the respective category page.
    * ![image](/waveandleaf/static/readme/recipes-button.png)
    * ![image](/waveandleaf/static/readme/my-recipes.png)
    * ![image](/waveandleaf/static/readme/my-recipes-2.png)

### Error Handling and User Alerts
* **404 Not Found:**
    * Navigated to a non-existent page to check the custom 404 page
    * ![image](/waveandleaf/static/readme/404.gif)
* **405 Method Not Allowed:**
    * Attempted unauthorized actions to check the custom 405 page. Confirmed the page displays correctly and automatically redirects to the home page.
    * ![image](/waveandleaf/static/readme/405.gif)
* **Wrong Username or Password:**
    * Used incorrect credentials during login to ensure the pop-up message appears, informing the user of incorrect login details.
    * ![image](/waveandleaf/static/readme/wrong.png)
* **Recipe Does Not Exist:**
    * Informing the user that the recipe does not exist.
    * ![image](/waveandleaf/static/readme/no-recipe.png)


# LightHouse Testing

## Both Desktop and Mobile version has been tested for the following:

* Site Performance
* Accessibility
* Best Practices
* Search Engine Optimization

### Desktop: <br>
![image](/waveandleaf/static/readme/lighthouse-desktop.png)
### Mobile: <br>
![image](/waveandleaf/static/readme/lighthouse-mobile.png)

#### Potential Changes for Mobile Optimization

* **Properly Size Images**: Compress and resize images to save 236 KiB.
* **Eliminate Render-Blocking Resources**: Defer or async load CSS/JS to save around 300 ms.


