import os
from flask import render_template, request, jsonify, session, flash, redirect, url_for
from waveandleaf import app, db
from waveandleaf.models import User, Category, Recipe, DifficultyLevel, CategoryName
# import bcrypt flask extension that provides bcrypt hashing utilities
from flask_bcrypt import Bcrypt

# home page
@app.route("/")
def home():
    return render_template("home.html")

# _________________________ CRUD ______________________________

@app.route('/upload-recipe', methods=['GET', 'POST'])
def upload_recipe():
    if not is_logged_in():
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        # get user_id from session
        user_id = session.get('user_id')
        if not user_id:
            flash('Your session has expired, please log in again.')
            return redirect(url_for('login'))
        # use the data from the form
        title = request.form['title']
        category_id = request.form['category_id']
        difficulty = request.form['difficulty']
        cooking_time = request.form['cooking_time']
        servings = request.form['servings']
        description = request.form['description']
        ingredients = request.form['ingredients']
        preparation_steps = request.form['preparation_steps']
        # this will be working with multiple selections
        allergens = request.form.getlist('allergens')
        image_url = request.form['image_url']

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
            user_id=session['user_id']
        )

        # add to the session and commit to the database
        db.session.add(new_recipe)
        db.session.commit()

        # todo: redirect to the recipe that's been created
        flash('Recipe uploaded successfully!')
        return redirect(url_for('home'))
    
    return render_template("upload-recipe.html")


# _________________________ CRUD ENDS ______________________________



# _________________________ authentication ______________________________

bcrypt = Bcrypt()
# todo: create a secret key for this in the env.py function
app.secret_key = os.environ.get("BCRYPT_SECRET_KEY")
# register
# create route for /register which will be triggered by the register button using js
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'error': 'Username already exists'}), 409
    ''' 
    this bcrypt function takes a plain text password as input and uses the bcrypt
    hashing algorithm to create a hash of the password. Hashing is a security measure
    to ensure that plain text passwords are not stored in the database, protecting them
    from being exposed even if the database is compromised.
    '''
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password_hash=hashed_password)
    # add user to db 
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Registered successfully. Please login.'}), 201

# login
# create route for /login which will be triggered by the login button using js
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    # if the user exist, present the message
    if user and bcrypt.check_password_hash(user.password_hash, password):
        # store user id in session
        session['user_id'] = user.id  
        # store username in session
        session['username'] = username
        return jsonify({'message': 'Logged in successfully!'}), 200
    # if the user doesn't exist, show error
    return jsonify({'error': 'Invalid username or password'}), 401

# return a boolean checking if the user logged in
def is_logged_in():
    return 'user_id' in session

# this returns the username for the welcome message
@app.route('/check-login', methods=['GET'])
def check_login():
    if is_logged_in():
        return jsonify({'logged_in': True, 'username': session['username']})
    else:
        return jsonify({'logged_in': False})
        
# log out
# the logout route removes the user from the session

@app.route('/logout', methods=['POST'])
def logout():
    # this will clear all the data in the session including flash messages user_id and username
    session.clear()  
    return jsonify({'redirect': url_for('home')})


# _________________________ authentication ends ______________________________