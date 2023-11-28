from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


app = Flask(__name__)
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maarket.db'
db.init_app(app)
login_manager.init_app(app)
bcrypt = Bcrypt(app)
from market import route
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

    


with app.app_context():
    from market.model import Item, User
    db.create_all()






