from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('bee', __name__)

@bp.route('/bee')
def index():
    db = get_db()
    Bees = db.execute(
        'SELECT bee_id, bee_type, dob, bee_name'
        ' FROM Bees'
        ' ORDER BY bee_id DESC'
    ).fetchall()
    return render_template('bee/index.html', Bees=Bees)


@bp.route('/createBee', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        bee_type = request.form['Bee type']
        dob = request.form['Date of Birth']
        bee_name = request.form['Bee Name']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (bee_type, dob, bee_name)'
                ' VALUES (?, ?, ?)',
                (bee_type, dob, g.Bees['bee_id'])
            )
            db.commit()
            return redirect(url_for('bee.index'))

    return render_template('bee/createBee.html')

def get_Bees(id):
    post = get_db().execute(
        'SELECT bee_id, bee_type, dob, bee_name'
        ' FROM Bees'
        ' ORDER BY bee_id DESC'
        (id,)
    ).fetchone()

    if Bees is None:
        abort(404, f"Bees bee_id {bee_id} doesn't exist.")

    return post
