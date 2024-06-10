import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://flaskapp:qwerty123@db:5432/rad"
    SQLALCHEMY_TRACK_MODIFICATIONS = False