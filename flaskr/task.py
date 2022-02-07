from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('task', __name__)

@bp.route('/task')
def index():
    db = get_db()
    Tasks = db.execute(
        'SELECT task_id, task_type, description, assignment_length'
        ' FROM Tasks'
        ' ORDER BY task_id DESC'
    ).fetchall()
    return render_template('task/index.html', Tasks=Tasks)


@bp.route('/createTask', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        task_type = request.form['task_type']
        description = request.form['description']
        assignment_length = request.form['assignment_length']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (task_type, description, assignment_length)'
                ' VALUES (?, ?, ?)',
                (task_type, description, g.Cells['task_id'])
            )
            db.commit()
            return redirect(url_for('task.index'))

    return render_template('task/createTask.html')

def get_Cells(id):
    post = get_db().execute(
        'SELECT task_id, task_type, description, assignment_length'
        ' FROM Tasks'
        ' ORDER BY task_id DESC'
        (id,)
    ).fetchone()

    if Cells is None:
        abort(404, f"Tasks task_id {task_id} doesn't exist.")

    return post