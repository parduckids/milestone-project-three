from waveandleaf import db

# import datetime for recipe class
from datetime import datetime
import enum


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    # use lazy='dynamic' performance optimization
    recipes = db.relationship("Recipe", backref="author", lazy="dynamic")

    def __repr__(self):
        return self.username


# enum ensures the 'category' field only accepts 3 values
# improving data accuracy and making checks simpler.
class CategoryName(enum.Enum):
    Vegan = "Vegan"
    Vegetarian = "Vegetarian"
    Pescatarian = "Pescatarian"


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # using Enum for category names as it's easier to maintain
    name = db.Column(db.Enum(CategoryName), unique=True, nullable=False)
    # use lazy='dynamic' performance optimization
    recipes = db.relationship("Recipe", backref="category", lazy="dynamic")

    def __repr__(self):
        return self.name


# enum ensures the 'difficulty' field only accepts 'Easy', 'Medium', or 'Hard'
# improving data accuracy and making checks simpler.
class DifficultyLevel(enum.Enum):
    Easy = "Easy"
    Medium = "Medium"
    Hard = "Hard"


class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    # using Enum for difficulty levels as it's easier to maintain
    difficulty = db.Column(db.Enum(DifficultyLevel), nullable=False)
    # URL for the main recipe image
    image_url = db.Column(db.String(255))
    description = db.Column(db.Text, nullable=False)
    # text field to list ingredients
    ingredients = db.Column(db.Text, nullable=False)
    # detailed preparation steps
    preparation_steps = db.Column(db.Text, nullable=False)
    cooking_time = db.Column(db.String(50))
    # number of servings per recipe
    servings = db.Column(db.Integer)
    uploaded_time = db.Column(db.DateTime, default=datetime.utcnow)
    edited_time = db.Column(db.DateTime, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    # username is added to present it on the recipes with 'created by'
    user = db.relationship("User", backref="user_recipes")
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    # allergens as a comma-separated list
    allergens = db.Column(db.String(255))

    def __repr__(self):
        return self.title
