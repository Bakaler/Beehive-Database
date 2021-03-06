from flask import(
    Blueprint, flash, g, redirect, render_template, url_for)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('bee', __name__)


@bp.route('/bee')
def index():
    db_connection = connect_to_database()
    query = 'SELECT bee_id, bee_type, dob, bee_name FROM Bees ORDER BY bee_id DESC;'
    result = execute_query(db_connection, query).fetchall();
    print(result)

    return render_template('bee/index.html', rows=result)

#TODO Figure out how to reroute after a creation
@bp.route('/createBee', methods=['GET', 'POST'])
def create():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'Select type_id, type_name FROM Bee_Types ORDER BY type_id ASC;'
        types = execute_query(db_connection, query).fetchall();
        return render_template('bee/createBee.html', types=types)
    elif request.method == 'POST':
        bee_type = request.form['bee_type']
        dob = request.form['dob']
        bee_name = request.form['bee_name']
        if bee_type == "None":
            query = 'INSERT INTO Bees (bee_type, dob, bee_name) VALUES (NULL,%s,%s)'
            data = (dob, bee_name)
        else:
            query = 'INSERT INTO Bees (bee_type, dob, bee_name) VALUES (%s,%s,%s)'
            data = (bee_type, dob, bee_name)
        execute_query(db_connection, query, data)

        return redirect(url_for('bee.index'))

def get_bee(bee_id, check_author=True):

    db_connection = connect_to_database()
    query = 'SELECT bee_id, bee_type, dob, bee_name FROM Bees WHERE bee_id = {};'.format(bee_id)
    bee = execute_query(db_connection, query).fetchone();
    if bee is None:
        abort(404, f"Bee ID {bee_id} doesn't exist.")

    return bee

@bp.route('/<int:bee_id>/updateBee', methods=('GET', 'POST'))
def update(bee_id):
    bee = get_bee(bee_id)
    db_connection = connect_to_database()

    if request.method == 'POST':
        bee_type = request.form['bee_type']
        dob = request.form['dob']
        bee_name = request.form['bee_name']

        if bee_type == "None":
            query = 'UPDATE Bees SET bee_type = NULL, dob = %s, bee_name = %s WHERE bee_id = %s;'
            data = (dob, bee_name, bee_id)
        else:
            query = 'UPDATE Bees SET bee_type = %s, dob = %s, bee_name = %s WHERE bee_id = %s;'
            data = (bee_type, dob, bee_name, bee_id)
        execute_query(db_connection, query, data)
        return redirect(url_for('bee.index'))

    query = 'Select type_id, type_name FROM Bee_Types ORDER BY type_id ASC;'
    types = execute_query(db_connection, query).fetchall();
    return render_template('bee/updateBee.html', bee=bee, types=types)

@bp.route('/<int:bee_id>/deleteBee', methods=('POST',))
def delete(bee_id):
    get_bee(bee_id)
    db = connect_to_database()
    query = 'DELETE FROM Bees WHERE bee_id = {}'.format(bee_id)
    execute_query(db, query)
    return redirect(url_for('bee.index'))


