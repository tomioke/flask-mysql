import os

basedir = os.path.abspath(os.path.dirname(__file__));

class Config(object):
    HOST = str(os.environ.get("CLEARDB_DATABASE_URL")); # Setting dari heroku
    DATABASE = str(os.environ.get("DB_DATABASE"));
    USERNAME = str(os.environ.get("DB_USERNAME"));
    PASSWORD = str(os.environ.get("DB_PASSWORD"));

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE;
    SQLALCHEMY_TRACK_NOTIFICATIONS = False;
    SQLALCHEMY_RECORD_QUERIES = True;