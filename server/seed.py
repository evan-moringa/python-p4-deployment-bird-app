# seed.py

from app import app, db
from models import Bird

# Initialize the app and the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birds.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Create all tables
with app.app_context():
    db.create_all()

    print('Deleting existing birds...')
    Bird.query.delete()

    print('Creating bird objects...')
    chickadee = Bird(
        name='Black-Capped Chickadee',
        species='Poecile Atricapillus',
        image='/images/black-capped-chickadee.jpeg'
    )
    grackle = Bird(
        name='Grackle',
        species='Quiscalus Quiscula',
        image='/images/grackle.jpeg'
    )
    starling = Bird(
        name='Common Starling',
        species='Sturnus Vulgaris',
        image='/images/starling.jpeg'
    )
    dove = Bird(
        name='Mourning Dove',
        species='Zenaida Macroura',
        image='/images/dove.jpeg'
    )

    print('Adding bird objects to transaction...')
    db.session.add_all([chickadee, grackle, starling, dove])
    print('Committing transaction...')
    db.session.commit()
    print('Complete.')
