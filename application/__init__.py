from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "the_key_is_a_secret"

from application import routes