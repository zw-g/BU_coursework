from flask import (
    render_template,
    redirect,
    url_for,
    session,
    Blueprint
)

from app.models.user import User
from app.models.vault import Vault

from app import constants

vault_bp = Blueprint(
    'vault',
    __name__,
    url_prefix='/vaults',
    template_folder='../templates'
)

@vault_bp.route('')
def vaults():
    """Handles displaying the user's vaults."""
    user = User.find_by_id(session['user_id'])
    encryption_key = session['encryption_key']

    # Fetch the user's vaults
    vaults = Vault.find_by_user(user.id, encryption_key)

    if constants.SINGLE_VAULT_MODE:
        default_vault = vaults[0]
        return redirect(url_for('vault.vault_item.vault_items', vault_id=default_vault.id))

    return render_template('/vaults/index.html', user=user, vaults=vaults)
