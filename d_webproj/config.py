import os

# old DB SQLite
class Config:
    # SECRET_KEY = os.environ.get("SECRET_KEY") or "this_should_be_a_secret_key"
    # SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'instance', 'database.db')}"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

# MSSQL
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://<USERNAME>:<PASSWORD>@<SERVER>/<DATABASE>?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"
