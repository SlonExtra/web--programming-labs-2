import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://ivan_ivanov_knowledge_base:your_password@localhost/ivan_ivanov_knowledge_base'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'