from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from main_app.db import get_db
from main_app.auth import login_required

bp = Blueprint('list', __name__)

@bp.route('/')
def index():
    db = get_db()
    movies = db.execute('SELECT title FROM movies ORDER BY title').fetchall()
    v_games = db.execute('SELECT title FROM v_games ORDER BY title').fetchall()
    music = db.execute('SELECT album FROM music ORDER BY album')
    return render_template('listing.html', movies = movies, v_games = v_games, music = music)


@bp.route('/add_media', methods=('GET', 'POST'))
@login_required
def add_media():
    if request.method == 'POST':

            return redirect(url_for('index'))

    return render_template('add_media.html')
