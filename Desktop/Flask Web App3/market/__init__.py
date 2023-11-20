from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "random string"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maarket.db'
    db.init_app(app)

    return app
    
app = create_app()

with app.app_context():
    from market.model import Item, User
    db.create_all()



