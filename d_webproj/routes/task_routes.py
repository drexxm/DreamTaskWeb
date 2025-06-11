from flask import Blueprint, render_template, request, redirect, url_for, abort
from models.task import Task, db
from flask_login import current_user, login_required

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/')
@login_required
def index():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks)

@task_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        task = Task(
            title=request.form['title'],
            status='pending',
            user_id=current_user.id  # ✅ ผูกกับผู้ใช้ปัจจุบัน
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task_bp.index'))
    return render_template('create.html')

@task_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    # task = Task.query.get(id) --> old code chg to connect user + task
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return abort(403)
    
    if request.method == 'POST':
        task.title = request.form['title']
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('task_bp.index'))
    return render_template('update.html', task=task)

@task_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    # task = Task.query.get(id) --> old code
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        return abort(403)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task_bp.index'))

@task_bp.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    # total = Task.query.count() --> chg to
    total = len(tasks)
    # completed = Task.query.filter_by(status='completed').count()
    # pending = Task.query.filter_by(status='pending').count()
    completed = sum(1 for t in tasks if t.status == 'completed')
    pending = total - completed
    return render_template('dashboard.html', total=total, completed=completed, pending=pending)
