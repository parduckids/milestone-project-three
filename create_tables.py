from waveandleaf import app, db

# create an application context
with app.app_context():
    # create all database tables
    db.create_all()