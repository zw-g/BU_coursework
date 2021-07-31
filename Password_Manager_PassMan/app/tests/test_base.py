import os
import flask_unittest
from .. import constants

# Note: Set the database filename in the environment
# before importing anything from the app package,
# so that the correct database file is created.
os.environ['DATABASE'] = constants.TEST_DATABASE
from app.app import app as flask_app
from app.db import _init_db, _seed_db


class TestBase(flask_unittest.ClientTestCase):
    app = flask_app  # required; assign the Flask app object

    def setUp(self, client):
        # Disable csrf protection
        self.app.config['WTF_CSRF_METHODS'] = []

        with self.app.app_context():
            _init_db()  # recreate the db schema before each test.

    def tearDown(self, client):
        pass

    # Helper for clients to seed the database
    def seed_db(self):
        with self.app.app_context():
            _seed_db()
