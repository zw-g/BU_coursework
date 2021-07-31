from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint
)

from app.models.user import User
from app.models.vault import Vault

from app.helpers.application_helper import (
    check_comlexity_requirements,
    get_encryption_key,
)

registration_bp = Blueprint(
  'registration',
  __name__,
  url_prefix='/registrations',
  template_folder='../templates'
)

@registration_bp.route('/new')
def new():
  """Handles GET/POST signup requests."""

  # Handle GET request
  return render_template('/registrations/new.html')


@registration_bp.route('/create', methods = ["POST"])
def create():
  username = request.form.get('username', '').strip()
  if not username:  # if username is empty
    return render_template(
      '/registrations/new.html',
      username_error='Please enter a username'
    )

  password = request.form.get('password')
  if not password:  # if password is empty
    return render_template(
      '/registrations/new.html',
      password_error='Please enter a password',
      username=username
    )
  try:
    check_comlexity_requirements(password)
  except RuntimeError as ex:
    return render_template(
      '/registrations/new.html',
      password_error=str(ex),
      username=username
    )

  retype_password = request.form.get('retype_password')
  if not retype_password:
    return render_template(
      '/registrations/new.html',
      retype_password_error='Please retype your password',
      username=username,
    )
  if retype_password != password:
    return render_template(
      '/registrations/new.html',
      retype_password_error='Passwords must match',
      username=username,
    )

  # Create the user
  try:
    User.create(username, password)
  except RuntimeError as ex:
    return render_template(
      '/registrations/new.html',
      error_message=str(ex)
    )

  # Create a default vault for the user
  user = User.find_by_username_password(username, password)
  if user is not None:
    encryption_key = get_encryption_key(password, user.salt)
    Vault.create(user.id, 'Default', 'Your default vault', encryption_key)

  # New user created, now send them back to the login page.
  return render_template(
    '/sessions/new.html',
    success_message='Account created!'
  )
