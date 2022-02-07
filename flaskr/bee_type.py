from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('bee_type', __name__)

@bp.route('/bee_type')
def index():
    db = get_db()
    Bee_Types = db.execute(
        'SELECT type_id, type_name, age, description'
        ' FROM Bee_Types'
        ' ORDER BY type_id DESC'
    ).fetchall()
    return render_template('bee_type/index.html', Bee_Types=Bee_Types)


@bp.route('/createBee_Type', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        type_name = request.form['type_name']
        age = request.form['age']
        description = request.form['description']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (type_name, age, description)'
                ' VALUES (?, ?, ?)',
                (type_name, age, description, g.Bee_Types['type_id'])
            )
            db.commit()
            return redirect(url_for('bee_type.index'))

    return render_template('bee_type/createBee_Type.html')

def get_Bee_Types(id):
    post = get_db().execute(
        'SELECT type_id, type_name, age, description'
        ' FROM Bee_Types'
        ' ORDER BY type_id DESC'
        (id,)
    ).fetchone()

    if Bee_Types is None:
        abort(404, f"Bee_Types type_id {type_id} doesn't exist.")

    return post