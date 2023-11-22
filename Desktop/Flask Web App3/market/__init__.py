from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()



app = Flask(__name__)
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maarket.db'
db.init_app(app)
from market import route

    


with app.app_context():
    from market.model import Item, User
    db.create_all()






