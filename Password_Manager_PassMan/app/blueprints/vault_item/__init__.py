import string
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    Blueprint
)

from app.models.user import User
from app.models.vault import Vault
from app.models.vault_item import VaultItem

from app import constants

item_bp = Blueprint(
    'vault_item',
    __name__,
    url_prefix="/<vault_id>/items",
    template_folder='../templates'
)

# vaults/<vault_id>/items
@item_bp.route('')
def vault_items(vault_id):
    """Handles displaying the vault's items."""
    user = User.find_by_id(session['user_id'])
    encryption_key = session['encryption_key']

    # Fetch the items for the specified vault
    items = VaultItem.find_by_vault(user.id, vault_id, encryption_key)
    return render_template(
        '/vault_items/index.html',
        user=user,
        items=items,
        vault_id=vault_id
    )

def render_view_vault_item_page(user, vault_id, item_id):
    encryption_key = session['encryption_key']

    """Renders the page to view/create a vault item."""
    if item_id == '0':  # Special case: user wants to create a new item
        # Only allow creating a new item in the user's own vault
        item = VaultItem.make_empty() if Vault.find_by_id(user.id, vault_id, encryption_key) else None
    else:  # Fetch the specific item from the specified vault
        item = VaultItem.find_by_id(user.id, vault_id, item_id, encryption_key)

    if item:
        item.password_has_digits = any(
            (char in string.digits) for char in item.password
        )
        item.password_has_special = any(
            (char in string.punctuation) for char in item.password
        )

    return render_template(
        '/vault_items/show.html',
        user=user,
        item=item,
        vault_id=vault_id,
        constants=constants,
    )

# /vaults/<vault_id>/items/<item_id>
@item_bp.route('/<item_id>', methods=['GET', 'POST'])
def vault_item(vault_id, item_id):
    """Handles viewing/creating/updating a vault item."""
    user = User.find_by_id(session['user_id'])
    encryption_key = session['encryption_key']

    if request.method == 'GET':  # Handle GET request
        return render_view_vault_item_page(user, vault_id, item_id)

    # Handle POST request
    assert request.method == 'POST'

    title = request.form.get('title', '').strip()
    website = request.form.get('website', '').strip()
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')  # don't strip spaces from password

    # TODO: Validate field lengths and render page with error message.

    if item_id == '0':  # Special case: user is creating an new item
        VaultItem.create(user.id, vault_id, title, website, username, password, encryption_key)
    else:
        VaultItem.update(user.id, vault_id, item_id, title, website, username, password, encryption_key)

    return redirect(url_for('vault.vault_item.vault_items', vault_id=vault_id))

# /vaults/<vault_id>/items/<item_id>/delete
@item_bp.route('/<item_id>/delete', methods=['POST'])
def delete_vault_item(vault_id, item_id):
    """Handles deleting a vault item."""
    user = User.find_by_id(session['user_id'])

    VaultItem.delete(user.id, vault_id, item_id)

    return redirect(url_for('vault.vault_item.vault_items', vault_id=vault_id))
