from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from models.user import User, db
from utils.decorators import admin_required
from werkzeug.security import generate_password_hash

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.route('/users')
@login_required
@admin_required
def manage_users():
    users = User.query.all()
    return render_template('admin_users.html', users=users)

@admin_bp.route('/add_user', methods=['GET', 'POST'])
@login_required
@admin_required
def add_user():
    if request.method == 'POST':
        hashed = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        new_user = User(
            username=request.form['username'],
            password=hashed,
            role=request.form['role']
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('admin_bp.manage_users'))
    return render_template('add_user.html')
