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
    query = 'SELECT bee_id, task_id FROM Bee_Tasks ORDER BY bee_id DESC;'
    result = execute_query(db_connection, query).fetchall();
    print(result)

    return render_template('bee_task/index.html', rows=result)


@bp.route('/createBee_Task', methods=['GET', 'POST'])
def create():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('/bee_task/createBee_Task.html')
    elif request.method == 'POST':
        bee_id = request.form['bee_id']
        task_id = request.form['task_id']
        query = 'INSERT INTO Bee_Tasks (bee_id, task_id) VALUES (%s, %s)'
        data = (bee_id, task_id)
        execute_query(db_connection, query, data)

        return redirect(url_for('bee_task.index'))

