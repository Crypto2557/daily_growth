import os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)

from app import routes