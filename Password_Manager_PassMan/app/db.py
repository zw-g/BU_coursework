import os
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

# Get the database filename from an environment variable.
# This is useful during testing.
DATABASE = os.environ.get('DATABASE', 'database.db')


def get_db():
    """Returns a (cached) connection to the database.
    The connection is created if it doesn't exist, then cached,
    and all subsequent calls return the cached connection.

    Returns:
        Connection: A (cached) connection to the database.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def _init_db():
    _exec_sql('schema.sql')


def _seed_db():
    # local import to avoid circular dependency
    from .helpers.db_helper import seed_db

    seed_db()


def _exec_sql(file):
    db = get_db()
    with current_app.open_resource(file) as f:
        db.executescript(f.read().decode('utf-8'))


def _close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@click.command('init-db')
@with_appcontext
def _init_db_command():
    _init_db()
    click.echo('Initialized the database')


@click.command('seed-db')
@with_appcontext
def _seed_db_command():
    _seed_db()
    click.echo('Seeded the database')


def init_app(app):
    app.cli.add_command(_init_db_command)
    app.cli.add_command(_seed_db_command)
    app.teardown_appcontext(_close_db)
