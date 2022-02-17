from flask import(
    Blueprint, flash, g, redirect, render_template, url_for)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('task_cell', __name__)


@bp.route('/task_cell')
def index():
    db_connection = connect_to_database()
    query = 'SELECT task_id, cell_id FROM Task_Cells ORDER BY task_id DESC;'
    result = execute_query(db_connection, query).fetchall();
    print(result)

    return render_template('task_cell/index.html', rows=result)


@bp.route('/createTask_Cell', methods=['GET', 'POST'])
def create():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT task_id, task_type FROM Tasks ORDER BY task_id ASC;'
        tasks = execute_query(db_connection, query).fetchall();
        query2 = 'SELECT cell_id, cell_type FROM Cells ORDER BY cell_id ASC;'
        cells = execute_query(db_connection, query2).fetchall();
        return render_template('/task_cell/createTask_Cell.html', tasks=tasks, cells=cells)
    elif request.method == 'POST':
        task_id = request.form['task_id']
        cell_id = request.form['cell_id']
        query = 'INSERT INTO Task_Cells (task_id, cell_id) VALUES (%s, %s)'
        data = (task_id, cell_id)
        execute_query(db_connection, query, data)

        return redirect(url_for('task_cell.index'))