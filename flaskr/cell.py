from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('cell', __name__)

@bp.route('/cell')
def index():
    db = get_db()
    Cells = db.execute(
        'SELECT cell_id, cell_type, location, size'
        ' FROM Cells'
        ' ORDER BY cell_id DESC'
    ).fetchall()
    return render_template('cell/index.html', Cells=Cells)


@bp.route('/createCell', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        cell_type = request.form['Cell type']
        location = request.form['Location']
        size = request.form['Size']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (cell_type, location, size)'
                ' VALUES (?, ?, ?)',
                (cell_type, location, g.Cells['cell_id'])
            )
            db.commit()
            return redirect(url_for('cell.index'))

    return render_template('cell/createCell.html')

def get_Cells(id):
    post = get_db().execute(
        'SELECT cell_id, cell_type, location, size'
        ' FROM Cells'
        ' ORDER BY cell_id DESC'
        (id,)
    ).fetchone()

    if Cells is None:
        abort(404, f"Cells cell_id {cell_id} doesn't exist.")

    return post