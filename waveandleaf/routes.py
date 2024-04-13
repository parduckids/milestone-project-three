from flask import render_template, request, jsonify
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
        
        return jsonify({'message': 'Logged in successfully!'}), 200
    # if the user doesn't exist, show error
    return jsonify({'error': 'Invalid username or password'}), 401




# _________________________ authentication ends ______________________________