from . import application_helper
from ..models.user import User
from ..models.vault import Vault
from ..models.vault_item import VaultItem


def seed_db():
    # Create a new user
    username, password = 'John', 'John123'
    User.create(username, password)
    user = User.find_by_username_password(username, password)
    encryption_key = application_helper.get_encryption_key(password, user.salt)

    # Create a vault for the user
    Vault.create(user.id, 'Personal', "John's personal credentials", encryption_key)
    vault = Vault.find_by_user(user.id, encryption_key)[0]

    # Create some vault items
    VaultItem.create(
        user.id,
        vault.id,
        title='My college account',
        website='https://www.bu.edu',
        username='john@gmail.com',
        password='bu123',
        encryption_key=encryption_key,
    )

    VaultItem.create(
        user.id,
        vault.id,
        title='My second email account',
        website='https://gmail.com',
        username='john',
        password='gmail123',
        encryption_key=encryption_key,
    )
