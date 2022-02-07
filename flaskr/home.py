from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    print("Hello")
    return render_template('home/index.html')