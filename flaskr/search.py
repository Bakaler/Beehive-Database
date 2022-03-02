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

    entity = request.args.get('entity')
    attribute = request.args.get('attribute')
    search_term = request.args.get('search_term')

    query = 'SELECT * FROM {} WHERE {}={}'.format(entity, attribute, search_term)
    result = execute_query(db_connection, query)

    query2 = 'DESCRIBE {}'.format(entity)
    result2 = execute_query(db_connection, query2)

    return render_template('search/results.html', rows=result, columns=result2)

