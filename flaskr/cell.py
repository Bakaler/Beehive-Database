from flask import(
    Blueprint, flash, g, redirect, render_template, url_for)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('cell', __name__)


@bp.route('/cell')
def index():
    db_connection = connect_to_database()
    query = 'SELECT cell_id, cell_type, location, size FROM Cells ORDER BY cell_id DESC;'
    result = execute_query(db_connection, query).fetchall();
    print(result)

    return render_template('cell/index.html', rows=result)


@bp.route('/createCell', methods=['GET', 'POST'])
def create():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('cell/createCell.html')
    elif request.method == 'POST':
        cell_type = request.form['cell_type']
        location = request.form['location']
        size = request.form['size']
        query = 'INSERT INTO Cells (cell_type, location, size) VALUES (%s,%s,%s)'
        data = (cell_type, location, size)
        execute_query(db_connection, query, data)

        return redirect(url_for('cell.index'))

def get_cell(cell_id):

    db_connection = connect_to_database()
    query = 'SELECT cell_id, cell_type, location, size FROM Cells ORDER BY cell_id DESC;'
    cell = execute_query(db_connection, query).fetchone();
    if cell is None:
        abort(404, f"Cell id {cell_id} doesn't exist.")

    return cell


@bp.route('/<int:cell_id>/updateCell', methods=('GET', 'POST'))
def update(cell_id):
    cell = get_cell(cell_id)

    if request.method == 'POST':
        cell_type = request.form['cell_type']
        location = request.form['location']
        size = request.form['size']
        error = None

        if not cell_type:
            error = 'cell_type is required'

        if not location:
            error += ' location is required'

        if not size:
            error += ' size is required'

        if error is not None:
            flash(error)

        else:
            db_connection = connect_to_database()
            query = 'UPDATE Cells SET cell_type = %s, location = %s, size = %s WHERE cell_id = %s;'
            data = (cell_type, location, size, cell_id)
            execute_query(db_connection, query, data)
            return redirect(url_for('cell.index'))

    return render_template('cell/updateCell.html', cell=cell)


@bp.route('/<int:cell_id>/deleteCell', methods=('POST',))
def delete(cell_id):
    get_cell(cell_id)
    db = connect_to_database()
    query = 'DELETE FROM Cells WHERE cell_id = {}'.format(cell_id)
    execute_query(db, query)
    return redirect(url_for('cell.index'))
    

