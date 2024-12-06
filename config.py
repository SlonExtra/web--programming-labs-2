import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://rudi:123@localhost/rudi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'секрет'
    DB_TYPE = 'postgres'