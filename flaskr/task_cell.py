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

    query = ("SELECT tc.task_id, t.task_type, tc.cell_id, c.cell_type "
            "FROM Task_Cells as tc "
            "inner join Tasks as t on t.task_id = tc.task_id "
            "inner join Cells as c on c.cell_id = tc.cell_id "
            "ORDER BY task_id DESC;")
    result = execute_query(db_connection, query).fetchall();

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


def get_task_cell(task_id, cell_id, check_author=True):
    db_connection = connect_to_database()
    query = 'SELECT task_id, cell_id FROM Task_Cells WHERE task_id = {} AND cell_id = {}'.format(task_id, cell_id)
    task_cell = execute_query(db_connection, query).fetchone();
    if task_cell is None:
        abort(404, f"Task_Cell with Task ID {task_id} and Cell ID {cell_id} doesn't exist.")

    return task_cell

@bp.route('/<int:task_id>/<int:cell_id>/updateTask_Cell', methods=('GET', 'POST'))
def update(task_id, cell_id):
    task_cell = get_task_cell(task_id, cell_id)

    if request.method == 'POST':
        task_id_n = request.form['task_id']
        cell_id_n = request.form['cell_id']
        error = None

        if not task_id_n:
            error = 'task_id is required'

        if not cell_id_n:
            error += ' cell_id is required'

        if error is not None:
            flash(error)

        else:
            db_connection = connect_to_database()
            query = 'UPDATE Task_Cells SET task_id = %s, cell_id = %s WHERE task_id = %s and cell_id = %s;'
            data = (task_id_n, cell_id_n, task_id, cell_id)
            execute_query(db_connection, query, data)
            return redirect(url_for('task_cell.index'))

    db_connection = connect_to_database()
    query = 'Select cell_id, cell_type FROM Cells ORDER BY cell_id ASC;'
    cells = execute_query(db_connection, query).fetchall();

    query = 'Select task_id, task_type FROM Tasks ORDER BY task_id ASC;'
    tasks = execute_query(db_connection, query).fetchall();
    return render_template('task_cell/updateTask_Cell.html', task_cell=task_cell, cells=cells, tasks=tasks)


@bp.route('/<int:task_id>/<int:cell_id>/deleteTask_Cell', methods=('POST',))
def delete(task_id, cell_id):
    get_task_cell(task_id, cell_id)
    db = connect_to_database()
    query = 'DELETE FROM Task_Cells WHERE task_id = {} AND cell_id = {}'.format(task_id, cell_id)
    execute_query(db, query)
    return redirect(url_for('task_cell.index'))