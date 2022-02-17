from flask import(
    Blueprint, flash, g, redirect, render_template, url_for)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('task', __name__)


@bp.route('/task')
def index():
    db_connection = connect_to_database()
    query = 'SELECT task_id, task_type, description, assignment_length FROM Tasks ORDER BY task_id DESC;'
    result = execute_query(db_connection, query).fetchall();
    print(result)

    return render_template('task/index.html', rows=result)

#TODO Figure out how to reroute after a creation
@bp.route('/createTask', methods=['GET', 'POST'])
def create():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('task/createTask.html')
    elif request.method == 'POST':
        task_type = request.form['task_type']
        description = request.form['description']
        assignment_length = request.form['assignment_length']
        query = 'INSERT INTO Tasks (task_type, description, assignment_length) VALUES (%s,%s,%s)'
        data = (task_type, description, assignment_length)
        execute_query(db_connection, query, data)

        return redirect(url_for('task.index'))

def get_task(task_id):

    db_connection = connect_to_database()
    query = 'SELECT task_id, task_type, description, assignment_length FROM Tasks WHERE task_id = {};'.format(task_id)
    task = execute_query(db_connection, query).fetchone();
    if task is None:
        abort(404, f"Task ID {task_id} doesn't exist.")

    return task

@bp.route('/<int:task_id>/updateTask', methods=('GET', 'POST'))
def update(task_id):
    task = get_task(task_id)

    if request.method == 'POST':
        task_type = request.form['task_type']
        description = request.form['description']
        assignment_length = request.form['assignment_length']
        error = None

        if error is not None:
            flash(error)

        else:
            db_connection = connect_to_database()
            query = 'UPDATE Tasks SET task_type = %s, description = %s, assignment_length = %s WHERE task_id = %s;'
            data = (task_type, description, assignment_length, task_id)
            execute_query(db_connection, query, data)
            return redirect(url_for('task.index'))

    return render_template('task/updateTask.html', task=task)

@bp.route('/<int:task_id>/deleteTask', methods=('POST',))
def delete(task_id):
    get_task(task_id)
    db = connect_to_database()
    query = 'DELETE FROM Tasks WHERE task_id = {}'.format(task_id)
    execute_query(db, query)
    return redirect(url_for('task.index'))


