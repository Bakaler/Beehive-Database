from flask import(
    Blueprint, flash, g, redirect, render_template, url_for)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('bee_type', __name__)


@bp.route('/bee_type')
def index():
    db_connection = connect_to_database()
    query = 'SELECT type_id, type_name, age, description FROM Bee_Types ORDER BY type_id DESC;'
    result = execute_query(db_connection, query).fetchall();
    print(result)

    return render_template('bee_type/index.html', rows=result)


@bp.route('/createBee_Type', methods=['GET', 'POST'])
def create():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('/bee_type/createBee_Type.html')
    elif request.method == 'POST':
        type_name = request.form['type_name']
        age = request.form['age']
        description = request.form['description']
        query = 'INSERT INTO Bee_Types (type_name, age, description) VALUES (%s, %s, %s)'
        data = (type_name, age, description)
        execute_query(db_connection, query, data)

        return redirect(url_for('bee_type.index'))


def get_bee_type(type_id, check_author=True):

    db_connection = connect_to_database()
    query = 'SELECT type_id, type_name, age, description FROM Bee_Types WHERE type_id = {};'.format(type_id)
    bee_type = execute_query(db_connection, query).fetchone();
    if bee_type is None:
        abort(404, f"Bee Type ID {type_id} doesn't exist.")

    return bee_type


@bp.route('/<int:type_id>/updateBee_Type', methods=('GET', 'POST'))
def update(type_id):
    bee_type = get_bee_type(type_id)

    if request.method == 'POST':
        type_name = request.form['type_name']
        age = request.form['age']
        description = request.form['description']
        error = None

        if not type_name:
            error = 'type_name is required'

        if not age:
            error += ' age is required'

        if not description:
            error += ' description is required'

        if error is not None:
            flash(error)

        else:
            db_connection = connect_to_database()
            query = 'UPDATE Bee_Types SET type_name = %s, age = %s, description = %s WHERE type_id = %s;'
            data = (type_name, age, description, type_id)
            execute_query(db_connection, query, data)
            return redirect(url_for('bee_type.index'))

    return render_template('bee_type/updateBee_Type.html', bee_type=bee_type)


@bp.route('/<int:type_id>/deleteBee_Type', methods=('POST',))
def delete(type_id):
    get_bee_type(type_id)
    db = connect_to_database()
    query = 'DELETE FROM Bee_Types WHERE type_id = {}'.format(type_id)
    execute_query(db, query)
    return redirect(url_for('bee_type.index'))

