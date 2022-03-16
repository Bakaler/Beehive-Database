from flask import(
    Blueprint, flash, g, redirect, render_template, url_for)
from flask import request
from werkzeug.exceptions import abort   #TODO Delete?
from flaskr.db import get_db            #TODO Delete?
from flaskr.db_connector import connect_to_database, execute_query


bp = Blueprint('search', __name__)

@bp.route('/search')
def index():
    return render_template('search/index.html')


@bp.route('/results/', methods=('GET', 'POST'))
def results():
    db_connection = connect_to_database()
    ints = ['bee_type', 'size', 'assignment_length']

    entity = request.args.get('entity')
    attribute = request.args.get('attribute')
    search_term = request.args.get('search_term')

    column_query = 'DESCRIBE {}'.format(entity)
    result2 = execute_query(db_connection, column_query)
    if search_term == '':
        query = f"SELECT * FROM {entity} WHERE {attribute} IS NULL"
    elif attribute[-2:] != 'id' and attribute not in ints:
        query = f"SELECT * FROM {entity} WHERE {attribute}='{search_term}'" 
    else:
        if search_term.isnumeric():
            query = 'SELECT * FROM {} WHERE {}={}'.format(entity, attribute, search_term)
        else:
            return render_template('search/results.html', rows=[], columns=result2)

    result = execute_query(db_connection, query)

    return render_template('search/results.html', rows=result, columns=result2)

