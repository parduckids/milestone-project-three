from flask import render_template, request, jsonify, session
from waveandleaf import app, db
from waveandleaf.models import User, Category, Recipe, DifficultyLevel
# import bcrypt flask extension that provides bcrypt hashing utilities
from flask_bcrypt import Bcrypt

# home page
@app.route("/")
def home():
    return render_template("home.html")



# _________________________ authentication ______________________________

bcrypt = Bcrypt()
# todo: create a secret key for this in the env.py function
app.secret_key = "secret"
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
    # remove user_id from session
    session.pop('user_id', None)
    # remove username from session
    session.pop('username', None)
    return jsonify({'message': 'Logged out successfully'}), 200



# _________________________ authentication ends ______________________________