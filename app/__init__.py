from flask import Flask
from .config import Config
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])

from app import views

migrate = Migrate(app, db) 
db = SQLAlchemy(app)
