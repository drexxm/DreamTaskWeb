from flask import Flask
from config import Config
from models.task import db
from routes.task_routes import task_bp
from models.user import User
from flask_login import LoginManager
from routes.auth_routes import auth


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(task_bp)
# for login
app.register_blueprint(auth) 

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    

# ===login part ===
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # redirect ถ้ายังไม่ได้ login
login_manager.init_app(app)

# โหลด user จาก session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

