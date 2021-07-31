from flask import Flask, g
from flask_wtf.csrf import CSRFProtect
import logging


def create_app():
    """Creates a Flask application, configures it, and returns it.

    Returns:
        Flask: The Flask application
    """
    app = Flask(__name__)

    # Register Blueprints
    from .blueprints.registrations import registration_bp
    from .blueprints.sessions import session_bp
    from .blueprints.vault import vault_bp
    from .blueprints.vault_item import item_bp
    
    vault_bp.register_blueprint(item_bp)

    app.register_blueprint(registration_bp)
    app.register_blueprint(session_bp)
    app.register_blueprint(vault_bp)

    # Setup secret key to some random bytes.
    # This is used for sessions and csrf protection.
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    # Enable logging
    logging.basicConfig(level=logging.DEBUG)

    # Note: We import db locally here because we want it to
    # delay loading the database filename from the enviroment
    # until this function is called.
    from . import db

    # Setup database
    with app.app_context():
        db.init_app(app)

    # Setup csrf protection
    CSRFProtect(app)

    return app
