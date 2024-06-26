import os
from flask import render_template, request, jsonify, session, flash
from flask import redirect, url_for
from waveandleaf import app, db
from waveandleaf.models import User, Category, Recipe, CategoryName
from waveandleaf.models import DifficultyLevel

# import bcrypt flask extension that provides bcrypt hashing utilities
from flask_bcrypt import Bcrypt

# home page


@app.route("/")
def home():
    return render_template("home.html")


# about us page


@app.route("/about")
def about():
    return render_template("about.html")


# recipe page
# this will present any recipe depending on recipe id


@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    # get the recipe from the database using the recipe ID
    recipe = Recipe.query.get(recipe_id)
    # if no recipe return error
    if recipe is None:
        return redirect(url_for("home", error="norecipe"))

    # pass the recipe data to the recipe template
    return render_template("recipe.html", recipe=recipe)


# my recipes page


@app.route("/my-recipes")
def my_recipes():
    if not is_logged_in():
        return redirect(url_for("home"))

    # get recipes that the current user created
    user_id = session["user_id"]
    user_recipes = Recipe.query.filter_by(user_id=user_id).all()

    return render_template("my_recipes.html", user_recipes=user_recipes)


# vegan category page
@app.route("/vegan")
def vegan_recipes():
    category = Category.query.filter_by(name=CategoryName.Vegan).first()
    vegan_recipes = Recipe.query.filter_by(category_id=1).all()
    return render_template("vegan_recipes.html", vegan_recipes=vegan_recipes)


# vegetarian category page


@app.route("/vegetarian")
def vegetarian_recipes():
    category = Category.query.filter_by(name=CategoryName.Vegetarian).first()
    vegetarian_recipes = Recipe.query.filter_by(category_id=2).all()
    return render_template(
        "vegetarian_recipes.html", vegetarian_recipes=vegetarian_recipes
    )


# pescatarian category page


@app.route("/pescatarian")
def pescatarian_recipes():
    category = Category.query.filter_by(name=CategoryName.Pescatarian).first()
    pescatarian_recipes = Recipe.query.filter_by(category_id=3).all()
    return render_template(
        "pescatarian_recipes.html", pescatarian_recipes=pescatarian_recipes
    )


# _________________________ CRUD ______________________________


# create
@app.route("/upload-recipe", methods=["GET", "POST"])
def upload_recipe():
    if not is_logged_in():
        return redirect(url_for("home"))

    if request.method == "POST":
        # get user_id from session
        user_id = session.get("user_id")
        if not user_id:
            flash("Your session has expired, please log in again.")
            return redirect(url_for("login"))
        # use the data from the form
        title = request.form["title"]
        category_id = request.form["category_id"]
        difficulty = request.form["difficulty"]
        cooking_time = request.form["cooking_time"]
        servings = request.form["servings"]
        description = request.form["description"]
        ingredients = request.form["ingredients"]
        preparation_steps = request.form["preparation_steps"]
        # this will be working with multiple selections
        allergens = request.form.getlist("allergens")
        image_url = request.form["image_url"]

        # create new recipe db instance
        new_recipe = Recipe(
            title=title,
            category_id=category_id,
            difficulty=difficulty,
            cooking_time=cooking_time,
            servings=servings,
            description=description,
            ingredients=ingredients,
            preparation_steps=preparation_steps,
            # store allergens as a comma-separated string
            allergens=", ".join(allergens),
            image_url=image_url,
            user_id=session["user_id"],
        )

        # add to the session and commit to the database
        db.session.add(new_recipe)
        db.session.commit()

        # display a js confirmation popup and redirect to home from there
        return render_template("upload-success.html")

    return render_template("upload-recipe.html")


# update
# edit recipe
@app.route("/edit-recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if not is_logged_in():
        return redirect(url_for("home"))

    # fetch the recipe from the database
    recipe = Recipe.query.get(recipe_id)
    # if no recipe, return error
    if recipe is None:
        return redirect(url_for("home", error="norecipe"))

    # check if the current user owns the recipe
    if recipe.user_id != session["user_id"]:
        # include SweetAlert in the HTML response
        edit_alert_script = """
        <script>
            window.onload = function() {
                Swal.fire({
                    title: 'Error!',
                    text: 'You do not have permission to edit this recipe.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                }).then(function() {
                    window.location.href = '/';
                });
            }
        </script>
        """
        return render_template(
            "home.html", recipe=recipe, edit_alert_script=edit_alert_script
        )

    if request.method == "POST":
        # update the recipe details with the form submission
        recipe.title = request.form["title"]
        recipe.category_id = request.form["category_id"]
        recipe.difficulty = request.form["difficulty"]
        recipe.cooking_time = request.form["cooking_time"]
        recipe.servings = request.form["servings"]
        recipe.description = request.form["description"]
        recipe.ingredients = request.form["ingredients"]
        recipe.preparation_steps = request.form["preparation_steps"]
        # update allergens as a comma-separated string
        recipe.allergens = ", ".join(request.form.getlist("allergens"))
        recipe.image_url = request.form["image_url"]

        # commit the changes to the database
        db.session.commit()

        # redirect to the My Recipes page
        return redirect(url_for("my_recipes"))

    # load the edit recipe template with the recipe details
    return render_template("edit-recipe.html", recipe=recipe)


# delete


@app.route("/delete_recipe/<int:recipe_id>", methods=["POST"])
def delete_recipe(recipe_id):
    if not is_logged_in():
        return redirect(url_for("home"))

    # get the recipe to delete
    recipe = Recipe.query.get(recipe_id)

    # todo: alert the user, no permission to delete
    # check if the current user owns the recipe
    if recipe.user_id != session["user_id"]:
        return redirect(url_for("my_recipes"))

    # delete the recipe
    db.session.delete(recipe)
    db.session.commit()

    return redirect(url_for("my_recipes"))


# _________________________ CRUD ENDS ______________________________


# _________________________ authentication ______________________________
bcrypt = Bcrypt()
# todo: create a secret key for this in the env.py function
app.secret_key = os.environ.get("BCRYPT_SECRET_KEY")
# register
# create route for /register which will be triggered by the reg button using js


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"error": "Username already exists"}), 409
    """
    this bcrypt function takes a plain text password as input and uses the
    bcrypt hashing algorithm to create a hash of the password. Hashing is a
    security measure to ensure that plain text passwords are not stored in
    the database, protecting them from being exposed even if the database is
    compromised.
    """
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(username=username, password_hash=hashed_password)
    # add user to db
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registered successfully. \n Please login."}), 201


# login
# create route for /login which will be triggered by the login button using js


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    # if the user exist, present the message
    if user and bcrypt.check_password_hash(user.password_hash, password):
        # store user id in session
        session["user_id"] = user.id
        # store username in session
        session["username"] = username
        return jsonify({"message": "Logged in successfully!"}), 200
    # if the user doesn't exist, show error
    return jsonify({"error": "Invalid username or password"}), 401


# return a boolean checking if the user logged in


def is_logged_in():
    return "user_id" in session


# this returns the username for the welcome message


@app.route("/check-login", methods=["GET"])
def check_login():
    if is_logged_in():
        return jsonify({"logged_in": True, "username": session["username"]})
    else:
        return jsonify({"logged_in": False})


# log out
# the logout route removes the user from the session


@app.route("/logout", methods=["POST"])
def logout():
    # this will clear all the data in the session
    session.clear()
    return jsonify({"redirect": url_for("home")})


# _________________________ authentication ends ______________________________


# 404


@app.errorhandler(404)
def page_not_found(e):
    # Note the 404 status explicitly supplied
    return render_template("404.html"), 404


# 405


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template("405.html"), 405
