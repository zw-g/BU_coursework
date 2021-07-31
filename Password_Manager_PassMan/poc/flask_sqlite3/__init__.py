import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(application.instance_path, 'flask_sqlite3.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        application.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        application.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(application.instance_path)
    except OSError:
        pass

    from flask_sqlite3 import db, app
    db.initialize_app(application)

    application.register_blueprint(app.bp)
    application.add_url_rule("/", endpoint="index")
    return application
