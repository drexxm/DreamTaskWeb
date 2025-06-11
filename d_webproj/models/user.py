from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from models import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # 🆔 Role ('user', 'admin')
    role = db.Column(db.String(10), default='user')