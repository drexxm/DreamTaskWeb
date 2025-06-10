import os

# old DB SQLite
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://3306:SmartAccess@2025@localhost/taskmanager1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"

    # SECRET_KEY = os.environ.get("SECRET_KEY") or "this_should_be_a_secret_key"
    # SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'instance', 'database.db')}"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
