from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "the_key_is_a_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@mysql:3306/flask-db"

# os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes, models