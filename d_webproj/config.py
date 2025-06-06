import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "this_should_be_a_secret_key"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'instance', 'database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'database.db')}"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
