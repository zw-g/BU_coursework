from dataclasses import asdict, dataclass
from ..test_base import TestBase
from ...models.user import User
from ...models.vault import Vault
from ...models.vault_item import VaultItem
from ...helpers import application_helper


@dataclass
class VaultItemData:
    title: str
    website: str
    username: str
    password: str


class TestVaultItem(TestBase):
    # Helper to create a user
    def create_user(self, username, password):
        User.create(username, password)
        user = User.find_by_username_password(username, password)
        self.assertIsNotNone(user)
        return user, application_helper.get_encryption_key(password, user.salt)

    # Helper to create a vault
    def create_vault(self, user_id, title, description, encryption_key):
        Vault.create(user_id, title, description, encryption_key)
        vaults = Vault.find_by_user(user_id, encryption_key)
        self.assertGreater(len(vaults), 0)
        vault = vaults[-1]
        self.assertIsNotNone(vault)
        return vault

    # Helper to validate vault item data
    def assert_vault_item_data(self, item: VaultItem, data: VaultItemData):
        self.assertIsNotNone(item)
        self.assertEqual(item.title, data.title)
        self.assertEqual(item.website, data.website)
        self.assertEqual(item.username, data.username)
        self.assertEqual(item.password, data.password)

    def test_create(self, client):
        with self.app.app_context():
            # Create a user with a vault
            jane, jane_encryption_key = self.create_user('Jane', 'Jane123')
            jane_vault = self.create_vault(jane.id, 'Default', 'My default vault', jane_encryption_key)

            # Add a vault item
            jane_item_data = VaultItemData(
                title='My college account',
                website='https://www.bu.edu',
                username='john@gmail.com',
                password='bu123',
            )
            VaultItem.create(jane.id, jane_vault.id, **asdict(jane_item_data), encryption_key=jane_encryption_key)

            # Check that the vault item was created
            items = VaultItem.find_by_vault(jane.id, jane_vault.id, jane_encryption_key)
            self.assertEqual(len(items), 1)
            self.assert_vault_item_data(items[0], jane_item_data)

            # Add another vault item
            jane_item_data2 = VaultItemData(
                title='My second email account',
                website='https://gmail.com',
                username='john',
                password='gmail123',
            )
            VaultItem.create(jane.id, jane_vault.id, **asdict(jane_item_data2), encryption_key=jane_encryption_key)

            # Check that we now have 2 vault items
            items = VaultItem.find_by_vault(jane.id, jane_vault.id, jane_encryption_key)
            self.assertEqual(len(items), 2)
            self.assert_vault_item_data(items[0], jane_item_data)
            self.assert_vault_item_data(items[1], jane_item_data2)

            # Create another user with a vault
            john, john_encryption_key = self.create_user('John', 'John123')
            john_vault = self.create_vault(john.id, 'Work', 'My work vault', john_encryption_key)

            # Add a vault item
            john_item_data = VaultItemData(
                title='My work account',
                website='https://www.bu.edu',
                username='john@bu.edu',
                password='bu123',
            )
            VaultItem.create(john.id, john_vault.id, **asdict(john_item_data), encryption_key=john_encryption_key)

            # Check that the vault item was created
            items = VaultItem.find_by_vault(john.id, john_vault.id, john_encryption_key)
            self.assertEqual(len(items), 1)
            self.assert_vault_item_data(items[0], john_item_data)

    def test_update(self, client):
        with self.app.app_context():
            # Create a user with a vault
            user, encryption_key = self.create_user('Jane', 'Jane123')
            vault = self.create_vault(user.id, 'Default', 'My default vault', encryption_key)

            # Add 2 vault items
            item_data = VaultItemData(
                title='My college account',
                website='https://www.bu.edu',
                username='john@gmail.com',
                password='bu123',
            )
            VaultItem.create(user.id, vault.id, **asdict(item_data), encryption_key=encryption_key)

            item_data2 = VaultItemData(
                title='My second email account',
                website='https://gmail.com',
                username='john',
                password='gmail123',
            )
            VaultItem.create(user.id, vault.id, **asdict(item_data2), encryption_key=encryption_key)

            # Check that the 2 vault items were created
            items = VaultItem.find_by_vault(user.id, vault.id, encryption_key)
            self.assertEqual(len(items), 2)
            self.assert_vault_item_data(items[0], item_data)
            self.assert_vault_item_data(items[1], item_data2)

            # Update the 2 vault items (swap them)
            item_data, item_data2 = item_data2, item_data
            VaultItem.update(user.id, vault.id, items[0].id, **asdict(item_data), encryption_key=encryption_key)
            VaultItem.update(user.id, vault.id, items[1].id, **asdict(item_data2), encryption_key=encryption_key)

            # Check that the 2 vault items were updated
            items = VaultItem.find_by_vault(user.id, vault.id, encryption_key)
            self.assertEqual(len(items), 2)
            self.assert_vault_item_data(items[0], item_data)
            self.assert_vault_item_data(items[1], item_data2)

    def test_delete(self, client):
        with self.app.app_context():
            # Create a user with a vault
            user, encryption_key = self.create_user('Jane', 'Jane123')
            vault = self.create_vault(user.id, 'Default', 'My default vault', encryption_key)

            # Add 2 vault items
            item_data = VaultItemData(
                title='My college account',
                website='https://www.bu.edu',
                username='john@gmail.com',
                password='bu123',
            )
            VaultItem.create(user.id, vault.id, **asdict(item_data), encryption_key=encryption_key)

            item_data2 = VaultItemData(
                title='My second email account',
                website='https://gmail.com',
                username='john',
                password='gmail123',
            )
            VaultItem.create(user.id, vault.id, **asdict(item_data2), encryption_key=encryption_key)

            # Check that the 2 vault items were created
            items = VaultItem.find_by_vault(user.id, vault.id, encryption_key)
            self.assertEqual(len(items), 2)
            self.assert_vault_item_data(items[0], item_data)
            self.assert_vault_item_data(items[1], item_data2)

            # Delete the first vault item
            VaultItem.delete(user.id, vault.id, items[0].id)

            # Check that the first vault item was deleted
            items = VaultItem.find_by_vault(user.id, vault.id, encryption_key)
            self.assertEqual(len(items), 1)
            self.assert_vault_item_data(items[0], item_data2)

    def test_find_by_vault(self, client):
        with self.app.app_context():
            # Create a user with a vault
            user, encryption_key = self.create_user('Jane', 'Jane123')
            vault = self.create_vault(user.id, 'Default', 'My default vault', encryption_key)

            # Add a vault item
            item_data = VaultItemData(
                title='My college account',
                website='https://www.bu.edu',
                username='john@gmail.com',
                password='bu123',
            )
            VaultItem.create(user.id, vault.id, **asdict(item_data), encryption_key=encryption_key)

            # Assume the id of an invalid user
            invalid_user_id = 2
            self.assertIsNone(User.find_by_id(invalid_user_id))

            # Assume the id of an invalid vault
            invalid_vault_id = 2
            self.assertTrue(vault.id != invalid_vault_id)

            # Find valid user's valid vault's items
            items = VaultItem.find_by_vault(user.id, vault.id, encryption_key)
            self.assertEqual(len(items), 1)
            self.assert_vault_item_data(items[0], item_data)

            # Find valid user's invalid vault's items
            items = VaultItem.find_by_vault(user.id, invalid_vault_id, encryption_key)
            self.assertEqual(len(items), 0)

            # Find invalid user's valid vault's items
            items = VaultItem.find_by_vault(invalid_user_id, vault.id, encryption_key)
            self.assertEqual(len(items), 0)

            # Find invalid user's invalid vault's items
            items = VaultItem.find_by_vault(invalid_user_id, invalid_vault_id, encryption_key)
            self.assertEqual(len(items), 0)

    def test_find_by_id(self, client):
        with self.app.app_context():
            # Create a user with a vault
            user, encryption_key = self.create_user('Jane', 'Jane123')
            vault = self.create_vault(user.id, 'Default', 'My default vault', encryption_key)

            # Add a vault item
            item_data = VaultItemData(
                title='My college account',
                website='https://www.bu.edu',
                username='john@gmail.com',
                password='bu123',
            )
            VaultItem.create(user.id, vault.id, **asdict(item_data), encryption_key=encryption_key)

            # Check that the vault item was created
            items = VaultItem.find_by_vault(user.id, vault.id, encryption_key)
            self.assertEqual(len(items), 1)
            item = items[0]
            self.assert_vault_item_data(item, item_data)

            # Assume the id of an invalid user
            invalid_user_id = 2
            self.assertIsNone(User.find_by_id(invalid_user_id))

            # Assume the id of an invalid vault
            invalid_vault_id = 2
            self.assertTrue(vault.id != invalid_vault_id)

            # Assume the id of an invalid vault item
            invalid_item_id = 2
            self.assertTrue(item.id != invalid_item_id)

            # Find valid user's valid vault's valid item
            found = VaultItem.find_by_id(user.id, vault.id, item.id, encryption_key)
            self.assertIsNotNone(found)
            self.assert_vault_item_data(found, item_data)

            # Check all combinations of valid/invalid user/vault/item ids
            for i in range(1, 8):
                user_id = invalid_user_id if (i & 1 << 2) else user.id
                vault_id = invalid_vault_id if (i & 1 << 1) else vault.id
                item_id = invalid_item_id if (i & 1 << 0) else item.id

                found = VaultItem.find_by_id(user_id, vault_id, item_id, encryption_key)
                self.assertIsNone(found)
