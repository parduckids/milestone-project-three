from waveandleaf import app, db
from waveandleaf.models import Category

# create an application context
with app.app_context():
    # create all database tables
    db.create_all()


    # define the category names and IDs
    categories = [
        {"name": "Vegan", "id": 1},
        {"name": "Vegetarian", "id": 2},
        {"name": "Pescatarian", "id": 3}
    ]

    # iterate over each category and add it to the database
    for category_data in categories:
        category = Category(
            id=category_data["id"],
            name=category_data["name"]
        )
        db.session.add(category)

    # commit the changes to the database
    db.session.commit()