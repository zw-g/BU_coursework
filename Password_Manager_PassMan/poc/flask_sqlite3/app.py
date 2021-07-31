from flask import Blueprint, render_template, request, redirect, url_for, current_app
import sqlite3 as sql
import flask_sqlite3.db as db

bp = Blueprint("app", __name__)

@bp.route("/")
def index():
    conn = db.get_database()
    conn.row_factory = sql.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")

    rows = cursor.fetchall()
    return render_template("index.html", rows = rows)

@bp.route('/create', methods = ['POST'])
def create():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            with db.get_database() as conn:
                conn.execute("INSERT INTO Users (username,password) VALUES (?,?)", (username, password))
                conn.commit()
                print("User successfully created")
        except:
            print("Error creating User")
            conn.rollback()
        
        finally:
            return redirect(url_for('index'))
