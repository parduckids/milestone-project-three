from flask import render_template
from waveandleaf import app, db
from waveandleaf.models import User, Category, Recipe, DifficultyLevel


@app.route("/")
def home():
    return render_template("home.html")