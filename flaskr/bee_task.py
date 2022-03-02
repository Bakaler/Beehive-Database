from flask import(
    Blueprint, flash, g, redirect, render_template, url_for)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('bee_task', __name__)


@bp.route('/bee_task')
def index():
    db_connection = connect_to_database()

    query = ("SELECT bt.bee_id, b.bee_name, bt.task_id, t.task_type "
            "FROM Bee_Tasks as bt "
            "inner join Bees as b on b.bee_id = bt.bee_id "
            "inner join Tasks as t on t.task_id = bt.task_id "
            "ORDER BY bee_id DESC;")
    result = execute_query(db_connection, query).fetchall();

    return render_template('bee_task/index.html', rows=result)


@bp.route('/createBee_Task', methods=['GET', 'POST'])
def create():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT bee_id, bee_name FROM Bees ORDER BY bee_id ASC;'
        bees = execute_query(db_connection, query).fetchall();
        query2 = 'SELECT task_id, task_type FROM Tasks ORDER BY task_id ASC;'
        tasks = execute_query(db_connection, query2).fetchall();
        return render_template('/bee_task/createBee_Task.html', bees=bees, tasks=tasks)
    elif request.method == 'POST':
        bee_id = request.form['bee_id']
        task_id = request.form['task_id']
        query = 'INSERT INTO Bee_Tasks (bee_id, task_id) VALUES (%s, %s)'
        data = (bee_id, task_id)
        execute_query(db_connection, query, data)
        return redirect(url_for('bee_task.index'))


def get_bee_task(bee_id, task_id, check_author=True):
    db_connection = connect_to_database()
    query = 'SELECT bee_id, task_id FROM Bee_Tasks WHERE bee_id = {} AND task_id = {};'.format(bee_id, task_id)
    bee_task = execute_query(db_connection, query).fetchone();
    if bee_task is None:
        abort(404, f"Bee_Task with Bee ID {bee_id} and Task ID {task_id} doesn't exist.")

    return bee_task


@bp.route('/<int:bee_id>/<int:task_id>/deleteBee_Task', methods=('POST',))
def delete(bee_id, task_id):
    get_bee_task(bee_id, task_id)
    db = connect_to_database()
    query = 'DELETE FROM Bee_Tasks WHERE bee_id = {} AND task_id = {}'.format(bee_id, task_id)
    execute_query(db, query)
    return redirect(url_for('bee_task.index'))

