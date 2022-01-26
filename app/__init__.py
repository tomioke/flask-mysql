from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # Membaca app
migrate = Migrate(app, db) # hubungkan app dengan db

from app.model import user, guru, siswa
from app import routes
