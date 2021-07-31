from app import create_app
from flask import (
    request,
    redirect,
    url_for,
    session,
)
from app.models.user import User
from . import constants

app = create_app()  # create our Flask application

@app.before_request
def check_authenticated():
    if request.endpoint not in constants.NON_AUTHENTICATED_ENDPOINTS:
        if 'user_id' not in session:  # user not logged in
            return redirect(url_for('session.new'))

        user = User.find_by_id(session['user_id'])
        if user is None:  # user doesn't exist anymore
            return redirect(url_for('session.new'))


@app.route('/')  # show the login page by default
def home():
    if 'user_id' in session:  # user already logged in
            app.logger.info('back to vault!')
            return redirect(url_for('vault.vaults'))
    
    return redirect(url_for('session.new'))
