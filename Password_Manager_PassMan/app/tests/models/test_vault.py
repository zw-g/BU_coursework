from ..test_base import TestBase
from ...models.user import User
from ...models.vault import Vault
from ...helpers import application_helper


class TestVault(TestBase):
    # Helper to create a user
    def create_user(self, username, password):
        User.create(username, password)
        user = User.find_by_username_password(username, password)
        self.assertIsNotNone(user)
        return user, application_helper.get_encryption_key(password, user.salt)

    # Helper to validate vault information
    def assert_vault_info(self, vault, title, description):
        self.assertIsNotNone(vault)
        self.assertEqual(vault.title, title)
        self.assertEqual(vault.description, description)

    def test_create(self, client):
        with self.app.app_context():
            # Create a user
            user, encryption_key = self.create_user('Jane', 'Jane123')

            # Create a vault for the user
            Vault.create(user.id, 'Default', 'My default vault', encryption_key)

            # Check that the vault was created
            vaults = Vault.find_by_user(user.id, encryption_key)
            self.assertEqual(len(vaults), 1)
            self.assert_vault_info(vaults[0], 'Default', 'My default vault')

            # Create another vault for the user
            Vault.create(user.id, 'Personal', 'My personal vault', encryption_key)

            # Check that we now have 2 vaults
            vaults = Vault.find_by_user(user.id, encryption_key)
            self.assertEqual(len(vaults), 2)
            self.assert_vault_info(vaults[0], 'Default', 'My default vault')
            self.assert_vault_info(vaults[1], 'Personal', 'My personal vault')

    def test_find_by_user(self, client):
        with self.app.app_context():
            # Create 2 users
            jane, jane_encryption_key = self.create_user('Jane', 'Jane123')
            john, john_encryption_key = self.create_user('John', 'John123')

            # Create some vaults for Jane
            Vault.create(jane.id, "Default", "Default vault", jane_encryption_key)
            Vault.create(jane.id, "Personal", "Personal vault", jane_encryption_key)

            # Create some vaults for John
            Vault.create(john.id, "Work", "Work vault", john_encryption_key)
            Vault.create(john.id, "School", "School vault", john_encryption_key)

            # Find vaults for Jane
            jane_vaults = Vault.find_by_user(jane.id, jane_encryption_key)
            self.assertEqual(len(jane_vaults), 2)
            self.assert_vault_info(jane_vaults[0], "Default", "Default vault")
            self.assert_vault_info(jane_vaults[1], "Personal", "Personal vault")

            # Find vaults for John
            john_vaults = Vault.find_by_user(john.id, john_encryption_key)
            self.assertEqual(len(john_vaults), 2)
            self.assert_vault_info(john_vaults[0], "Work", "Work vault")
            self.assert_vault_info(john_vaults[1], "School", "School vault")

    def test_find_by_invalid_user(self, client):
        with self.app.app_context():
            # Create a user with a vault
            user, encryption_key = self.create_user('Jane', 'Jane123')
            Vault.create(user.id, 'Default', 'My default vault', encryption_key)

            # Assume the id of an invalid user
            invalid_user_id = 2
            self.assertIsNone(User.find_by_id(invalid_user_id))

            # Check that no vaults are returned for an invalid user
            vaults = Vault.find_by_user(invalid_user_id, encryption_key)
            self.assertEqual(len(vaults), 0)

    def test_find_by_id(self, client):
        with self.app.app_context():
            # Create 2 users
            jane, jane_encryption_key = self.create_user('Jane', 'Jane123')
            john, john_encryption_key = self.create_user('John', 'John123')

            # Create some vaults for Jane
            Vault.create(jane.id, "Default", "Default vault", jane_encryption_key),
            Vault.create(jane.id, "Personal", "Personal vault", jane_encryption_key),
            jane_vaults = Vault.find_by_user(jane.id, jane_encryption_key)

            # Create some vaults for John
            Vault.create(john.id, "Work", "Work vault", john_encryption_key),
            Vault.create(john.id, "School", "School vault", john_encryption_key),
            john_vaults = Vault.find_by_user(john.id, john_encryption_key)

            # Find vaults for Jane by id
            for vault in jane_vaults:
                found = Vault.find_by_id(jane.id, vault.id, jane_encryption_key)
                self.assert_vault_info(found, vault.title, vault.description)

            # Find vaults for John by id
            for vault in john_vaults:
                found = Vault.find_by_id(john.id, vault.id, john_encryption_key)
                self.assert_vault_info(found, vault.title, vault.description)

    def test_find_by_invalid_id(self, client):
        with self.app.app_context():
            # Create a user with a vault
            user, encryption_key = self.create_user('Jane', 'Jane123')
            Vault.create(user.id, 'Default', 'My default vault', encryption_key)
            vaults = Vault.find_by_user(user.id, encryption_key)
            self.assertEqual(len(vaults), 1)
            vault = vaults[0]
            self.assert_vault_info(vault, 'Default', 'My default vault')

            # Assume the id of an invalid user
            invalid_user_id = 2
            self.assertIsNone(User.find_by_id(invalid_user_id))

            # Assume the id of an invalid vault
            invalid_vault_id = 2
            self.assertTrue(vault.id != invalid_vault_id)

            # Find valid user's valid vault by id
            found = Vault.find_by_id(user.id, vault.id, encryption_key)
            self.assert_vault_info(found, 'Default', 'My default vault')

            # Find valid user's invalid vault by id
            found = Vault.find_by_id(user.id, invalid_vault_id, encryption_key)
            self.assertIsNone(found)

            # Find invalid user's valid vault by id
            found = Vault.find_by_id(invalid_user_id, vault.id, encryption_key)
            self.assertIsNone(found)

            # Find invalid user's invalid vault by id
            found = Vault.find_by_id(invalid_user_id, invalid_vault_id, encryption_key)
            self.assertIsNone(found)
