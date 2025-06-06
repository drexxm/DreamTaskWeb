from flask import Blueprint, render_template, request, redirect, url_for
from models.task import Task, db
from flask_login import login_required

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@task_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        new_task = Task(title=title, status='pending')
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('task_bp.index'))
    return render_template('create.html')

@login_required
@task_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('task_bp.index'))
    return render_template('update.html', task=task)

@login_required
@task_bp.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('task_bp.index'))

@login_required
@task_bp.route('/dashboard')
def dashboard():
    total = Task.query.count()
    completed = Task.query.filter_by(status='completed').count()
    pending = Task.query.filter_by(status='pending').count()
    return render_template('dashboard.html', total=total, completed=completed, pending=pending)
