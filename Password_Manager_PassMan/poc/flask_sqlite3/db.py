import sqlite3

import click
from flask import Flask, g, current_app
from flask.cli import with_appcontext

app = Flask(__name__)
DATABASE = 'database.db'

def get_schema():
    f = open('schema.sql', 'r')
    with f:
        data = f.read()
        return data

def get_database():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

def initialize_database():
    db = get_database()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('initialize-database')
@with_appcontext
def initialize_database_command():
    initialize_database()
    click.echo("Initialized the database")

def close_database(exception=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def initialize_app(app):
    app.teardown_appcontext(close_database)
    app.cli.add_command(initialize_database_command)
