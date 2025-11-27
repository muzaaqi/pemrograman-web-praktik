import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    HOST = os.environ.get('DB_HOST')
    DATABASE = os.environ.get('DB_DATABASE')
    USERNAME = os.environ.get('DB_USERNAME')
    PASSWORD = os.environ.get('DB_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True