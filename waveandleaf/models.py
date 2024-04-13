from waveandleaf import db


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    # use lazy='dynamic' performance optimization
    recipes = db.relationship('Recipe', backref='author', lazy='dynamic')  

    def __repr__(self):
        return self.username


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # use lazy='dynamic' performance optimization
    recipes = db.relationship('Recipe', backref='category', lazy='dynamic') 

    def __repr__(self):
        return self.name

