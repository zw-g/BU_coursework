from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    Blueprint
)
from app.models.user import User
from ...helpers import application_helper

session_bp = Blueprint(
  'session',
  __name__,
  url_prefix='/sessions',
  template_folder='../templates'
)

@session_bp.route('/new')
def new():
  """Handles GET/POST new session requests."""
  return render_template('/sessions/new.html')


@session_bp.route('/create', methods = ["POST"])
def create():
  username = request.form.get('username', '').strip()
  if not username:  # username is empty
    return render_template(
      '/sessions/new.html',
      username_error='Please enter a username'
    )

  password = request.form.get('password')
  if not password:  # password is empty
    return render_template(
      '/sessions/new.html',
      password_error='Please enter a password',
      username=username
    )

  # Check if the user exists
  user = User.find_by_username_password(username, password)
  if user is None:  # no such user was found
    return render_template(
      '/sessions/new.html',
      error_message='Invalid username or password'
    )

  # User exists; log them in
  session['user_id'] = user.id
  session['encryption_key'] = application_helper.get_encryption_key(password, user.salt)

  return redirect(url_for('vault.vaults'))


@session_bp.route('/delete')
def delete():
  # Clear the session, and send the user back to the login screen
  session.pop('user_id', None)
  session.pop('encryption_key', None)

  return redirect(url_for('session.new'))