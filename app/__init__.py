from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
import logging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # Membaca app
migrate = Migrate(app, db) # hubungkan app dengan db

# Menampilkan pesan error pada heroku
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

from app.model import user, guru, siswa
from app import routes

if __name__ == '__main__':
    app.run(debug=True)
