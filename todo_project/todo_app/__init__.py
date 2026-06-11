from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


def create_app(config):
    app = Flask(__name__)
    app.config.update(config)
    return app


def get_db(app=None):
    db = SQLAlchemy(app)
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    return db


# @TODO: Move these param values to .env file
config = dict(SECRET_KEY = "45cf93c4d41348cd9980674ade9a7356",
              SQLALCHEMY_DATABASE_URI = "sqlite:///site.db")
app = create_app(config)
db = get_db(app)
migrate = Migrate(app, db) # Initialize Flask-Migrate

login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# Always put Routes at end
from todo_app import routes