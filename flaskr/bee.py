from flask import (
    Blueprint, flash, g, redirect, render_template, url_for
)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('bee', __name__)


@bp.route('/bee')
def index():
    print("Hello")
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
        return render_template('bee/createBee.html')
    elif request.method == 'POST':
        bee_type = request.form['bee_type']
        dob = request.form['dob']
        bee_name = request.form['bee_name']
        query = 'INSERT INTO Bees (bee_type, dob, bee_name) VALUES (%s,%s,%s)'
        data = (bee_type, dob, bee_name)
        execute_query(db_connection, query, data)

        return render_template('bee/createBee.html')


