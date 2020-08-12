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
    return render_template('listing.html', movies = movies, v_games = v_games)


@bp.route('/add_movies', methods=('GET', 'POST'))
def add_movies():
    if request.method == 'POST':
        name = request.form["title"]
        error = None
        if not name:
            error = "Title is required."
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO v_games title VALUES ?'(name,))
            db.commit()
            return redirect(url_for('index'))

    return render_template('add_media.html', media = 'Movies')


@bp.route('/add_v_games', methods=('GET', 'POST'))
def add_v_games():
    if request.method == 'POST':
        name = request.form["title"]
        error = None
        if not name:
            error = "Title is required."
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO v_games title VALUES ?', (name,))
            db.commit()
            return redirect(url_for('index'))

    return render_template('add_media.html', media = 'Video Games')


@bp.route('/add_music', methods=('GET','POST'))
def add_music():
    if request.method == 'POST':
        album = request.form["album"]
        artist = request.form["artist"]
        error = None
        if not album:
            error = "album is required."
        if not artist:
            error = "artist is required."
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE music SET album = ?, artist = ?'
                (album, artist)
            )
            db.commit()
            return redirect(url_for('index'))

    return render_template('add_music.html')
